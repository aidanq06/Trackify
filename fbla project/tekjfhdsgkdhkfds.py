# Import the required modules
import sqlite3
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ctk
import random as rand
import matplotlib.pyplot as plt
import pyautogui as pg
import tkinter.font as font
from PIL import ImageTk, Image
# Please make sure the required modules are installed on the computer you are using

dimensions = pg.size()
dimensions_string = str(dimensions[0]) + "x" + str(dimensions[1])
x = dimensions[0]
y = dimensions[1]

# Create a student class with the attributes "first" "last" and "grade" correlating to the students first and last name as well as the students grade
class student():
    def __init__(self, first, last, grade, number):
        self.first = first
        self.last = last
        self.grade = grade
        self.number = number

# Error Window (input an error message argument to display)
def error(error=str):

    def close():
        eWin.destroy()

    eWin = ctk.CTkToplevel()
    eWin.title("Error!")
    eWin.geometry("400x100")

    Label = ctk.CTkLabel(eWin, text=error,corner_radius=10)
    Label.place(relx=0.5,rely=.3, anchor=CENTER)
    
    close_button = ctk.CTkButton(eWin, text="Close", command=close)
    close_button.place(relx=0.5,rely=0.7, anchor=CENTER)

# Success Window (input a success message argument to display)
def success(success=str):

    def close():
        sWin.destroy()

    sWin = ctk.CTkToplevel()
    sWin.title("Success!")
    sWin.geometry("400x100")

    Label = ctk.CTkLabel(sWin, text=success,corner_radius=10)
    Label.place(relx=0.5,rely=.3, anchor=CENTER)
    
    close_button = ctk.CTkButton(sWin, text="Close", command=close)
    close_button.place(relx=0.5,rely=0.7, anchor=CENTER)

    # Define a function to be called when the "edit student" button is clicked
    
def inputStudent():

    # Create a new top-level window (i.e., a new window that is independent of the main window)
    inputStudent = ctk.CTkToplevel()
    inputStudent.title("Enter New Student")
    inputStudent.geometry("200x275")

    # Add three labels and three entry widgets to the input window
    first_name = ctk.CTkLabel(inputStudent, text="Enter the student's name.")
    first_name.pack()
    first_entry = ctk.CTkEntry(inputStudent)
    first_entry.pack()

    last_name = ctk.CTkLabel(inputStudent, text="Enter the student's last name.")
    last_name.pack()
    last_entry = ctk.CTkEntry(inputStudent)
    last_entry.pack()

    grade_label = ctk.CTkLabel(inputStudent, text="Select the student's grade")
    grade_label.pack()
    grade_level = ctk.IntVar(inputStudent)
    grade_level.set("Select a grade.")
    grade_options = ctk.CTkComboBox(master=inputStudent, values=["9", "10", "11", "12"], variable=grade_level)
    grade_options.pack()

    var1 = ctk.IntVar()
    var1.set(1)
    cb = ctk.CTkCheckBox(master= inputStudent, text= "Ignore duplicate students", variable= var1, checkbox_height=20, checkbox_width=20)
    cb.place(relx= .1, rely= .7)

    # Define a function to be called when the "Save" button is clicked
    def save_inputs():
        try:
            # If the user didn't input anything for firstname or lastname, bring up an error.
            if first_entry.get() == "" or last_entry.get() == "":
                error("Please fill in all fields!")
            else:
                # Generate a random student id
                studentID = tk.IntVar()
                studentID.set(rand.randint(0,100000))

                # Get the values entered in the entry widgets
                new_student = student(first_entry.get(), last_entry.get(), int(grade_level.get()), studentID)
                    
                # Save the values to database
                cursor.execute("SELECT * FROM students WHERE grade = 12 OR 11 OR 10 OR 9")
                students =cursor.fetchall()
                student_first = new_student.first.capitalize()
                student_last = new_student.last.capitalize()
                if var1.get() == 0 or len(students) == 0:
                    cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?)", (student_first, student_last, new_student.grade, 0, studentID.get()))
                else:
                    for option in range(len(students)):
                        if students[option][4] == studentID.get():
                            studentID.set(rand.randint(0, 100000))
                    if not(new_student.first.capitalize() == students[option][0] and new_student.last.capitalize() == students[option][1] and new_student.grade == students[option][2]):
                        cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?)", (student_first, student_last, new_student.grade, 0, studentID.get()))
                    else:
                        ...
                conn.commit()

                # Close the input window
                inputStudent.destroy()
                success(f"Successfully added {student_first} {student_last} ({grade_level.get()}) to the database.")

        except:
            error("Please fill in all fields!")

    # Add a "Save" button to the input window
    save_button = ctk.CTkButton(inputStudent, text="Submit", command=save_inputs)
    save_button.place(relx= .15, rely=0.85)

def report():
    def destroyGui():
        dialog_box.destroy()

    def save_inputs():
        try:
            dialog_box.destroy()
            choice = grade_level.get()
            cursor.execute("SELECT * FROM students WHERE grade = :grade", {'grade': choice})
            fetch = cursor.fetchall()
            points = list()
            name = list()
            for i in range(len(fetch)):
                points.append(fetch[i][3])
                name.append(f"{fetch[i][0]} {(fetch[i][1][0]).title()}.")
                #print(fetch[i][3],fetch[i][0])
            name2=list()
            for i in range(len(name)):
                name2.append(f"{name[i]} ({points[i]} points)")
            if points==[] and name==[]:
                error(f"There currently isn't any data for grade {choice}.")
            else:
                plt.rcParams["figure.figsize"] = (15,5)
                plt.barh(name2,points,color="royalblue")

                #plt.plot(range(len(data)), data,"r+")
                plt.savefig(f"QuarterlyG{choice}.pdf",format="pdf")

                plt.title(f'Quarterly Points (Grade {choice})', fontweight="bold")

                plt.ylabel('Students', fontweight="bold")
                plt.xlabel('Points', fontweight="bold")

                plt.show()
        except TclError: # didnt select a grade
            error("Please select a grade.")

    #GUI    
    dialog_box = ctk.CTkToplevel()
    dialog_box.title("Dialog Box")
    dialog_box.geometry("400x100")

    #dropdown menu for grade selection
    dropdown = ctk.CTkLabel(dialog_box, text="Select which grade level's quarterly report you would like to view.")
    dropdown.pack()
    grade_level = ctk.IntVar(dialog_box)
    grade_level.set("Select a grade.")
    dropdown = ctk.CTkComboBox(master=dialog_box, values=["9", "10", "11", "12"], variable=grade_level)
    dropdown.pack()

    # Submit grade button
    save_button = ctk.CTkButton(dialog_box, text="Submit", command=save_inputs)
    save_button.place(relx=0.75,rely=0.75,anchor=CENTER)

    #quit the view students GUI
    save_button = ctk.CTkButton(dialog_box, text="Quit", command=destroyGui)
    save_button.place(relx=0.25,rely=0.75,anchor=CENTER)

#command for pick winners button
def pickWinner():
    prizes = ["free spirit gear", "a day of excused school", "free admission to all school games for a quarter", "free lunch for a week"]
    studentValues = list()
    cursor.execute("SELECT * FROM students")
    all_students = cursor.fetchall()
    pointList = list()
    maxStudents = list()
    max = all_students[0][3]
    for i in range(len(all_students)):
        pointList.append((all_students[i][3],all_students[i][4]))
        if all_students[i][3] > max:
            max = all_students[i][3]
    for i in range(len(all_students)):
        if max == all_students[i][3]:
            maxStudents.append(all_students[i])
    
    # GUI
    win = ctk.CTkToplevel()
    win.title("Winners")
    win.geometry("400x800")

    #prints the winner if there is multiple winners
    if len(maxStudents) > 1:
        Label2 = ctk.CTkLabel(win, text= "These students tied for first place: ", corner_radius=10)
        Label2.pack()
        for i in range(len(maxStudents)):
            Label = ctk.CTkLabel(win, text=f" {(maxStudents[i][0]).title()} {(maxStudents[i][1][0]).title()}. with a total of: {maxStudents[i][3]} points.", corner_radius=10)
            Label.pack()

    #prints the winner if there is only one winner
    else:
        Label3 = ctk.CTkLabel(win, text= "The student that won first place is: ", corner_radius=10)
        Label3.pack()

        Label4 = ctk.CTkLabel(win, text=f" {(maxStudents[0][0]).title()} {(maxStudents[0][1][0]).title()}. with a total of: {maxStudents[0][3]} points.", corner_radius=10)
        Label4.pack()

    try:
        #picks a random winner for each grade level
        for grade in range(9, 13):
            cursor.execute("SELECT * FROM students WHERE grade = :grade", {'grade': grade})
            gradeStudents = cursor.fetchall()
            randStudent = rand.randint(0, len(gradeStudents)-1)
            studentValues.append(gradeStudents[randStudent])
            space = ctk.CTkLabel(win, text= " ")
            space.pack()
            label5= ctk.CTkLabel(win, text= "The random winner for grade " + str(grade) + " is: ")
            label5.pack()
            label6 = ctk.CTkLabel(win, text= f" {(gradeStudents[randStudent][0]).title()} {(gradeStudents[randStudent][1][0]).title()}. with a total of: {gradeStudents[randStudent][3]} points.")
            label6.pack()  

        space1 = ctk.CTkLabel(win, text= "")
        space1.pack()
        space2 = ctk.CTkLabel(win, text= "")
        space2.pack()
        rand.shuffle(studentValues)

        if len(maxStudents) > 1:
            label7 = ctk.CTkLabel(win, text= " These students won a Pizza Party for their class: ")
            label7.pack()
            for i in range(len(maxStudents)):
                Label10 = ctk.CTkLabel(win, text=f" {(maxStudents[i][0]).title()} {(maxStudents[i][1][0]).title()}. ", corner_radius=10)
                Label10.pack()

    #prints the winner if there is only one winner
        else:
            Label11 = ctk.CTkLabel(win, text= "This student won a Pizza Party for their class: ", corner_radius=10)
            Label11.pack()

            Label12 = ctk.CTkLabel(win, text=f" {(maxStudents[0][0]).title()} {(maxStudents[0][1][0]).title()}.", corner_radius=10)
            Label12.pack()

        for i in range(len(studentValues)):
            label14 = ctk.CTkLabel(win, text="")
            label14.pack()
            label13 = ctk.CTkLabel(win, text=str(studentValues[i][0]) + " " + str(studentValues[i][1][0]) + ". wins " + prizes[i])
            label13.pack()
        


    except ValueError:
        ...

#creates the home GUI
root = tk.Tk()
root.geometry(dimensions_string)
root.state('zoomed')
root.configure(bg= '#1c1c1c')
default_font = ctk.CTkFont(size= 18, family= 'Roboto')
large_font = ctk.CTkFont(size= 25, family= 'Roboto')


def refresh_treeview():
    for item in listbox.get_children():
        listbox.delete(item)

    conn = sqlite3.connect('studentDatabase.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE grade = 12 OR 11 OR 10 OR 9 OR 8 OR 7 OR 6")
    students = cursor.fetchall()

    for student in students:
        listbox.insert('', 'end', values=(student))
    listbox.place(x= 350, y = 300, anchor= "nw")

style = ttk.Style(root)
style.theme_use("clam")
ttk.Style().configure("Treeview", fieldbackground= "#242424", background = "#242424", foreground= "#9b9a92")
ttk.Style().configure("Treeview.Heading", background = "#242424", foreground= "#9b9a92", relief= "flat")

style.configure("Treeview", rowheight= 25)
# Assign the listbox widget number of columns and names of columns
listbox = ttk.Treeview(root, selectmode="extended",columns=("c1", "c2", "c3", "c4", "c5"),show="headings", height= 12)
listbox.column("# 1", anchor=CENTER, width = 300)
listbox.heading("# 1", text="First Name")
listbox.column("# 2", anchor=CENTER, width = 300)
listbox.heading("# 2", text="Last Name")
listbox.column("# 3", anchor=CENTER, width = 300)
listbox.heading("# 3", text="Grade Level")
listbox.column("# 4", anchor=CENTER, width = 300)
listbox.heading("# 4", text="Points")
listbox.column("# 5", anchor=CENTER, width = 300)
listbox.heading("# 5", text="Student id")


refresh_treeview()


def edit_student():
    def update_student():
        # If user leaves both entries empty nothing will happen
        if first_entry.get() == "" and last_entry.get() == "":
            ...
        else:
            # Sets Student first and last name to the user inputs
            cursor.execute("UPDATE students SET name = :first, lastname = :last, grade = :grade  WHERE number = :number", {'first':(first_entry.get()).title(), 'last': (last_entry.get()).title(), 'grade': int(grade_options.get()), 'number': selection[4] })
        
        # Saves changes to the database
        conn.commit()
        # Closes the edit window and refreshes the dialog box
        edit_window.destroy()
        refresh_treeview()

    # Gets the user selection
    item = listbox.selection()
    if len(item) == 1:
        selection = listbox.item(item, option="values")

        # Creates the edit window
        edit_window= ctk.CTkToplevel()
        edit_window.title("edit student")

        # Label and entry for student's first name
        first_name = ctk.CTkLabel(edit_window, text="Edit student's first name")
        first_name.pack()
        first_entry = ctk.CTkEntry(edit_window, placeholder_text= selection[0])
        first_entry.pack()

        # Label and entry for students's last name
        last_name = ctk.CTkLabel(edit_window, text="Edit student's last name")
        last_name.pack()
        last_entry = ctk.CTkEntry(edit_window, placeholder_text= selection[1])
        last_entry.pack()

        # label and dropdown menu for student's grade
        grade_label = ctk.CTkLabel(edit_window, text="Edit student's grade")
        grade_label.pack()
        grade_level = ctk.IntVar(edit_window)
        grade_options = ctk.CTkComboBox(master=edit_window, values=["9", "10", "11", "12"], variable=grade_level)
        grade_options.set(selection[2])
        grade_options.pack()
        
        # Saves the entries and updates the student
        b1 = ctk.CTkButton(edit_window, text= "submit", command=update_student)
        b1.pack()
    else:
        error("Please select someone.")

# Create a function to remove one or more students using selection
def remove_student():
    items = listbox.selection()
    if len(items) != 0:
        for i in items:
            selection = listbox.item(i, option="values")
            last_name = selection[1]
            first_name = selection[0]
            student_number = selection[4]
            cursor.execute("DELETE FROM students WHERE name = :first AND lastname = :last AND number = :studentnumber",{'first': first_name, 'last': last_name, 'studentnumber': student_number})
        conn.commit()     
        # Close dialog box (to update database) then reopen to show the result.
        refresh_treeview()
    else:
        error("Please select someone.")
    


# Creates a function to remove all students
def remove_everyone():
    def makingSure():
        cursor.execute("DELETE FROM students")
        conn.commit()
    refresh_treeview()

    # Creates a window to confirm the option to delete all students
    sure = ctk.CTkToplevel(root)
    sure.title("")
    sure.geometry("300x100")
    message = ctk.CTkLabel(sure, text= "Are you sure you want to remove all students?")
    message.pack()

    # Function to close the confirm window
    def closeSure():
        sure.destroy()

    # Yes and no buttons to confirm deletion of all students
    b1 = ctk.CTkButton(sure, text= "Yes", command= makingSure)
    b1.pack()
    b2 = ctk.CTkButton(sure, text= "No", command= closeSure)
    b2.pack()
    


# Add points to a selected student
def add_points():
    def check_for_points():
        x=first_entry.get()
        y=last_entry.get()

        # Statements to decide the amount of points to add to a student
        if x == "Select an event " or y == "Did the student attend or participate in this event?":
            error("Please fill out all fields.")
        else: 
            if x == " School Prom" or x == " School Dance Performance" or x == " School Pep Rally" or x == " School Homecoming" or x == " School Musical":
                if y == " Attended":
                    points = 10
                elif y == " Participated": 
                    points = 15
            elif x == " School Soccer Game" or x == " School Football Game" or x == " School Lacross Game" or x == " School Basketball Game" or x == " School Volleyball Game":
                if y == " Attended":
                    points = 5
                elif y == " Participated":
                    points = 10
            
            # Assigns points to the selected student
            cursor.execute("SELECT * FROM students WHERE name = :first AND lastname = :last", {'first':first_name,'last':last_name})
            fetch = cursor.fetchall()
            cursor.execute("SELECT points FROM students WHERE number = :number", {'number': number})
            temp_points =cursor.fetchall()
            point_value = int(temp_points[0][0]) + points
            cursor.execute("UPDATE students SET points = :point WHERE number = :number", {'point': point_value, 'number': number })
            conn.commit()
            
            # Destroy dialog box (to update database) then reopen to show the result. Destroy new points GUI.
            new_points.destroy()
            refresh_treeview()

            # Success window prints student name and points assigned
            success(f"Assigned {fetch[0][0]} {fetch[0][1][0]}. {points} points")



    def clear_points():
        #removes all points from the selected student
        cursor.execute("UPDATE students SET points = :point WHERE number = :number", {'point': 0, 'number': number })
        conn.commit()

        # Destroy dialog box (to update database) then reopen to show the result. Destroy new points GUI.
        new_points.destroy()
        refresh_treeview()

    try:
        #Gets the selected student and sets it to selection
        items = listbox.selection()
        selection = listbox.item(items, option="values")
    except:
        # Error message if multiple students were selected
        error("You can only add points to one student at a time.")
    try:
        #Sets first, last and student number to according variables
        last_name = selection[1]
        first_name = selection[0]
        number = selection[4]

        # Creates the window to add points to the selected student
        new_points= ctk.CTkToplevel()
        new_points.title("Add points to student")
        new_points.geometry("350x150")

        # Dropdown for the event the selected student attended
        l1 = ctk.CTkLabel(new_points, text= "What event did  " + first_name + " " + last_name + " attend or participate in")
        l1.pack()
        event_check = ctk.IntVar(new_points)
        event_check.set("Select an event ")
        first_entry = ctk.CTkComboBox(master=new_points, values=[" School Prom", " School Dance Performance", " School Pep Rally", " School Homecoming", " School Musical", " School Soccer Game", " School Football Game", " School Lacross Game", " School Basketball Game", " School Volleyball Game"], variable=event_check, width= 325)
        first_entry.pack()

        # Dropdown for whether the selected student participated or attended the selected event
        type_check = ctk.IntVar(new_points)
        type_check.set("Did the student attend or participate in this event?")
        last_entry = ctk.CTkComboBox(master=new_points, values=[" Attended", " Participated"], variable=type_check, width= 325)
        last_entry.pack()

        # Submit selections for the event and whether the student attended or participated in the event
        submit = ctk.CTkButton(new_points, text= "Submit", command=check_for_points)
        submit.pack()
        clear = ctk.CTkButton(new_points, text= "Clear student's points", command= clear_points)
        clear.pack()

    # index error
    except:
        # error message in nobody is selected
        error("Please select someone")

def get_entry():
    last_name = searchbar.get()
    for item in listbox.get_children():
        listbox.delete(item)
    root.update_idletasks()
    cursor.execute("SELECT * FROM students WHERE lastname = :last", {'last': last_name.capitalize()})
    temp_values= cursor.fetchall()
    for values in temp_values:
        listbox.insert('', 'end', values=(values))
    root.update_idletasks()

def clear():
    refresh_treeview()
    searchbar.delete(0, END)

def open_help_window():
    def close_help_window():
        help_frame.place_forget()
        help_button['image'] = help_image

    if (help_button.cget('image')=='pyimage2'):
        help_frame.place(x= 1800, y= 25, anchor=NE)
        help_button['image'] = help2_image
    else:
        close_help_window()
        
#creates a label for the home GUI called Student Involment Tracker
left_frame = Frame(root, width = 275, height = 1000, bg= '#242424')
left_frame.place(x = 0, y= 0, anchor = NW)

image_frame = Frame(root, width = 2000, height = 100, bg= '#1c1c1c')
image_frame.place(x = 275, y= 100, anchor = NW)

top_frame = Frame(root, width = 2000, height = 100, bg= '#1c1c1c')
top_frame.place(x = 275, y= 0, anchor = NW)


img = ImageTk.PhotoImage(Image.open("banner.png"))
image = Label(image_frame, image = img, border= 0)
image.pack()

# Add a "Edit Student" button to the dialog box
edit_button = ctk.CTkButton(root, text="Edit Student", command=edit_student)
edit_button.place(x= 420, y= 600, height= 35, width = 200)

# Add a "remove student" button to the dialog box
remove_button = ctk.CTkButton(root, text="Remove student", command= remove_student)
remove_button.place(x= 670, y= 600, height= 35, width = 200)

# Add a "Edit student points" button to the dialog box
add_points_button = ctk.CTkButton(root, text= "Edit student points", command= add_points)
add_points_button.place(x= 920, y= 600, height= 35, width = 200)

# Add a "remove all" button to the dialog box
remove_all = ctk.CTkButton(root, text="Remove all", command= remove_everyone)
remove_all.place(x= 1170, y= 600, height= 35, width = 200)

# Add a search bar to the dialog box
searchbar = ctk.CTkEntry(root, placeholder_text= "Search by last name: ")
searchbar.place(x= 850, y= 540, height= 25, width= 500, anchor= CENTER)

enter = ctk.CTkButton(root, text= "Enter", command= get_entry)
enter.place(x = 1200, y= 540, height= 25, width= 120, anchor= CENTER)

clear = ctk.CTkButton(root, text= "Clear", command= clear)
clear.place(x = 500, y= 540, height= 25, width= 120, anchor= CENTER)


help_image = PhotoImage(file = "help_image.png")
help2_image = PhotoImage(file = "help2_image.png")

help_button = tk.Button(root, image= help_image,command=open_help_window, bg="#1c1c1c", fg= "#9b9a92", font= large_font, bd = 0, anchor = "w")
help_button.place(x= 1800, y= 25, anchor=NW)
help_frame = Frame(root, width = 500, height = 900, bg= '#242424')

# Allows you to add new students to the database
add_student = tk.Button(root, text="Add new student",command=inputStudent, width=22, bg="#242424", fg= "#9b9a92", font= default_font, bd = 0, anchor = "w")
add_student.place(x= 30, y= 50, anchor=NW)

# Creates a report of the entire database
winner_button = tk.Button(root, text="Pick Winner", command=pickWinner, width=22, bg="#242424", fg= "#9b9a92", font= default_font, bd = 0, anchor= "w")
winner_button.place(x= 30, y= 150, anchor=NW)

# Creates a report of the entire database
report_button = tk.Button(root, text="Create Report", command=report, width=22, bg="#242424", fg= "#9b9a92", font= default_font, bd = 0, anchor= "w")
report_button.place(x= 30, y= 250, anchor=NW)

#closes the application
quit_button = tk.Button(root, text="Quit", command=root.destroy, width=22, bg="#242424", fg= "#9b9a92", font= default_font, bd = 0, anchor= "w")
quit_button.place(x= 25, y= 900, anchor=NW)

#connects to the database
conn = sqlite3.connect('studentDatabase.db')

#creates a cursor
cursor = conn.cursor()

# Create the table
cursor.execute('''CREATE TABLE IF NOT EXISTS students (name TEXT, lastname TEXT, grade INTEGER, points INTEGER, number INTEGER)''')

# Commit the changes to the database
conn.commit()

# keeps gui running
if __name__ == "__main__":
    root.mainloop()

    #closes the cursor
    cursor.close()

    #closes the connection
    conn.close()