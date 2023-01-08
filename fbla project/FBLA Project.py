# Import the required modules
import sqlite3
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ctk
import random as rand
import matplotlib.pyplot as plt

# FIRST TIME RUN
"""
# Connect to the database
conn = sqlite3.connect('studentDatabase.db')
# Create a cursor
cursor = conn.cursor()
# Create the table
cursor.execute('''CREATE TABLE students (name TEXT, lastname TEXT, grade INTEGER, points INTEGER, number INTEGER)''')
# Commit the changes to the database
conn.commit()
# Close the connection to the database
conn.close()
"""



"""
Must have at least five sporting events and five non-sports school events.
1.  School prom
2.  School dance performance
3.  School pep rally
4.  School homecoming
5.  School musical
ideas:spelling bee

1.  School soccer games
2.  School football games
3.  School lacross games
4.  School basketball
5.  School volleyball
"""

global student_number
#create a student class with the attributes "first" "last" and "grade" correlating to the students first and last name as well as the students grade
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

    style = ttk.Style(eWin)
    style.theme_use("clam")

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

    style = ttk.Style(sWin)
    style.theme_use("clam")

    Label = ctk.CTkLabel(sWin, text=success,corner_radius=10)
    Label.place(relx=0.5,rely=.3, anchor=CENTER)
    
    close_button = ctk.CTkButton(sWin, text="Close", command=close)
    close_button.place(relx=0.5,rely=0.7, anchor=CENTER)
    

def open_dialog_box():
    # Create a new top-level window (i.e., a new window that is independent of the main window)
    dialog_box = ctk.CTkToplevel()
    dialog_box.title("Dialog Box")
    dialog_box.geometry("800x325")

    # Create a list of students
    cursor.execute("SELECT * FROM students WHERE grade = 12 OR 11 OR 10 OR 9 OR 8 OR 7 OR 6")
    options = cursor.fetchall()

    # Create a variable to store the selected options
    selected_options = tk.StringVar(value=options)

    # Create a listbox widget to display the options
    style = ttk.Style(root)
    style.theme_use("clam")
    ttk.Style().configure("Treeview", fieldbackground= "#242424", background = "#242424", foreground= "white")
    ttk.Style().configure("Treeview.Heading", background = "#242424", foreground= "white", relief= "flat")

    listbox = ttk.Treeview(dialog_box, selectmode="extended",columns=("c1", "c2", "c3", "c4"),show="headings")
    listbox.column("# 1", anchor=CENTER)
    listbox.heading("# 1", text="First Name")
    listbox.column("# 2", anchor=CENTER)
    listbox.heading("# 2", text="Last Name")
    listbox.column("# 3", anchor=CENTER)
    listbox.heading("# 3", text="Grade Level")
    listbox.column("# 4", anchor=CENTER)
    listbox.heading("# 4", text="Points")

    for option in options:
        listbox.insert('', 'end', values=(option))
    listbox.place(relx= 0, rely= .1)

    # Define a function to be called when the "Save" button is clicked
    def edit_student():
        def update_student():
            cursor.execute("UPDATE students SET name = :first, lastname = :last, grade = :grade  WHERE number = :number", {'first': entry1.get(), 'last': entry2.get(), 'grade': int(entry3.get()), 'number': selection[4] })
            conn.commit()
            edit_window.destroy()
            dialog_box.destroy()


        item = listbox.selection()
        selection = listbox.item(item, option="values")
        print(selection)

        edit_window= ctk.CTkToplevel()
        edit_window.title("edit student")

        label1 = ctk.CTkLabel(edit_window, text="Edit student's first name")
        label1.pack()
        entry1 = ctk.CTkEntry(edit_window, placeholder_text= selection[0])
        entry1.pack()

        label2 = ctk.CTkLabel(edit_window, text="Edit student's last name")
        label2.pack()
        entry2 = ctk.CTkEntry(edit_window, placeholder_text= selection[1])
        entry2.pack()

        label3 = ctk.CTkLabel(edit_window, text="Edit student's grade")
        label3.pack()
        grade_level = ctk.IntVar(edit_window)
        entry3 = ctk.CTkComboBox(master=edit_window, values=["6", "7", "8", "9", "10", "11", "12"], variable=grade_level)
        entry3.set(selection[2])
        entry3.pack()

        b1 = ctk.CTkButton(edit_window, text= "submit", command= update_student)
        b1.pack()

    #create a function to remove one or more students using selection
    def remove_student():
        items = listbox.selection()
        for i in items:
            selection = listbox.item(i, option="values")
            temp_name = selection[1]
            temp_name2 = selection[0]
            student_number = selection[4]
            cursor.execute("DELETE FROM students WHERE name = :first AND lastname = :last AND number = :studentnumber",{'first': temp_name2, 'last': temp_name, 'studentnumber': student_number})
        conn.commit()     
        
        # Destroy dialog box (to update database) then reopen to show the result.
        dialog_box.destroy()
        open_dialog_box()

    #creates a function to remove all students
    def remove_everyone():
        cursor.execute("DELETE FROM students")
        conn.commit()

        # Destroy dialog box (to update database) then reopen to show the result.
        dialog_box.destroy()
        open_dialog_box()


    def add_points():
        def check_for_points():
            x = entry1.get()
            y= entry2.get()
            print(x)
            print(y)


            if x == " School prom" or x == " School dance performance" or x == " School pep rally" or x == " School homecoming" or x == " School musical":
                if entry2.get() == "attended":
                    points = 10
                else: 
                    points = 15
            else: 
                if entry2.get() == "attended":
                    points = 5
                else:
                    points = 10
            cursor.execute("SELECT points FROM students WHERE number = :number", {'number': number})
            temp_points =cursor.fetchall()
            point_value = int(temp_points[0][0]) + points
            cursor.execute("UPDATE students SET points = :point WHERE number = :number", {'point': point_value, 'number': number })
            conn.commit()
            
            # Destroy dialog box (to update database) then reopen to show the result. Destroy new points GUI.
            new_points.destroy()
            dialog_box.destroy()
            open_dialog_box()


        def clear_points():
            cursor.execute("UPDATE students SET points = :point WHERE number = :number", {'point': 0, 'number': number })
            conn.commit()

            # Destroy dialog box (to update database) then reopen to show the result. Destroy new points GUI.
            new_points.destroy()
            dialog_box.destroy()
            open_dialog_box()

        items = listbox.selection()
        selection = listbox.item(items, option="values")

        # ERROR: Didn't pick a student
        try:
            temp_name = selection[1]
        except IndexError:
            error("test")
        temp_name2 = selection[0]
        number = selection[4]

        new_points= ctk.CTkToplevel()
        new_points.title("add points to student")
        new_points.geometry("350x150")
        l1 = ctk.CTkLabel(new_points, text= "What event did  " + temp_name2 + " " + temp_name + " attend or participate in")
        l1.pack()
        event_check = ctk.IntVar(new_points)
        event_check.set("Select an event ")
        entry1 = ctk.CTkComboBox(master=new_points, values=[" School Prom", " School Dance Performance", " School Pep Rally", " School Homecoming", " School Musical", " School Soccer Game", " School Football Game", " School Lacross Game", " School Basketball Game", " School Volleyball Game"], variable=event_check, width= 325)
        entry1.pack()
        type_check = ctk.IntVar(new_points)
        type_check.set("did the student attend or participate in this event ")
        entry2 = ctk.CTkComboBox(master=new_points, values=["Attended", "Participated"], variable=type_check, width= 325)
        entry2.pack()
        submit = ctk.CTkButton(new_points, text= "Submit", command= check_for_points)
        submit.pack()
        clear = ctk.CTkButton(new_points, text= "Clear student's points", command= clear_points)
        clear.pack()

    def get_entry():
        temp_name = my_entry.get()
        for item in listbox.get_children():
            listbox.delete(item)
        dialog_box.update_idletasks()
        cursor.execute("SELECT * FROM students WHERE lastname = :last", {'last': temp_name.capitalize()})
        temp_values= cursor.fetchall()
        for values in temp_values:
            listbox.insert('', 'end', values=(values))
        dialog_box.update_idletasks()

    def destroy():
        dialog_box.destroy()




    # Add a "Save" button to the dialog box
    save_button = ctk.CTkButton(dialog_box, text="Edit Student", command=edit_student)
    save_button.place(relx= .01, rely= .85)

    # Add a "remove student" button to the dialog box
    remove_button = ctk.CTkButton(dialog_box, text="Remove student", command= remove_student)
    remove_button.place(relx= .265, rely= .85)

    # add a "remove all" button to the dialog box
    remove_all = ctk.CTkButton(dialog_box, text="Remove all", command= remove_everyone)
    remove_all.place(relx= .52, rely= .85)

    add_points_button = ctk.CTkButton(dialog_box, text= "Edit student points", command= add_points)
    add_points_button.place(relx= .775, rely= .85)

    my_entry = ctk.CTkEntry(dialog_box, placeholder_text= "Search by last name: ")
    my_entry.place(relx= .15, rely= .02, height= 25, width= 500)


    my_button = ctk.CTkButton(dialog_box, text= "Enter", command= get_entry)
    my_button.place(relx = .8, rely= .02, height= 25, width= 120)

    my_button2 = ctk.CTkButton(dialog_box, text= "Clear", command=lambda:[destroy(),open_dialog_box()])
    my_button2.place(relx = .02, rely= .02, height= 25, width= 80)
    
def inputStudent():

    # not used?
    def optionmenu_get(choice):
        grade_level = choice

    # Create a new top-level window (i.e., a new window that is independent of the main window)
    inputStudent = ctk.CTkToplevel()
    inputStudent.title("Enter New Student")
    inputStudent.geometry("200x275")

    # Add three labels and three entry widgets to the input window
    label1 = ctk.CTkLabel(inputStudent, text="Enter the student's name.")
    label1.pack()
    entry1 = ctk.CTkEntry(inputStudent)
    entry1.pack()

    label2 = ctk.CTkLabel(inputStudent, text="Enter the student's last name.")
    label2.pack()
    entry2 = ctk.CTkEntry(inputStudent)
    entry2.pack()

    label3 = ctk.CTkLabel(inputStudent, text="Select the student's grade")
    label3.pack()
    grade_level = ctk.IntVar(inputStudent)
    grade_level.set("Select a grade.")
    entry3 = ctk.CTkComboBox(master=inputStudent, values=["6", "7", "8", "9", "10", "11", "12"], variable=grade_level)
    entry3.pack()

    var1 = ctk.IntVar()
    var1.set(1)
    cb = ctk.CTkCheckBox(master= inputStudent, text= "Ignore duplicate students", variable= var1, checkbox_height=20, checkbox_width=20)
    cb.place(relx= .1, rely= .7)

    # Define a function to be called when the "Save" button is clicked
    def save_inputs():
        try:
            # If the user didn't input anything for firstname or lastname, bring up an error.
            if entry1.get() == "" or entry2.get() == "":
                error("Please fill in all fields!")
            else:
                #if entry1.get() == ""
                # Generate a random student id
                studentID = tk.IntVar()
                studentID.set(rand.randint(0,100000))

                # Get the values entered in the entry widgets
                new_student = student(entry1.get(), entry2.get(), int(grade_level.get()), studentID)
                    
                # Save the values to database
                cursor.execute("SELECT * FROM students WHERE grade = 12 OR 11 OR 10 OR 9 OR 8 OR 7 OR 6")
                options =cursor.fetchall()
                student_first = new_student.first.capitalize()
                student_last = new_student.last.capitalize()
                if var1.get() == 0 or len(options) == 0:
                    cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?)", (student_first, student_last, new_student.grade, 0, studentID.get()))
                else:
                    for option in range(len(options)):
                        if options[option][4] == studentID.get():
                            studentID.set(rand.randint(0, 100000))
                    if not(new_student.first.capitalize() == options[option][0] and new_student.last.capitalize() == options[option][1] and new_student.grade == options[option][2]):
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
                print(fetch[i][3],fetch[i][0])
            print(points,name)

            plt.rcParams["figure.figsize"] = (15,5)
            plt.barh(name,points,color="royalblue")

            #plt.plot(range(len(data)), data,"r+")
            plt.savefig(f"QuarterlyG{choice}.pdf",format="pdf")

            plt.title(f'Quarterly Points (Grade {choice})', fontweight="bold")

            plt.ylabel('Students', fontweight="bold")
            plt.xlabel('Points', fontweight="bold")

            plt.show()
        except TclError: # didnt select a grade
            error("Please select a grade.")
        
    dialog_box = ctk.CTkToplevel()
    dialog_box.title("Dialog Box")
    dialog_box.geometry("400x100")

    dropdown = ctk.CTkLabel(dialog_box, text="Select which grade level's quarterly report you would like to view.")
    dropdown.pack()
    grade_level = ctk.IntVar(dialog_box)
    grade_level.set("Select a grade.")
    dropdown = ctk.CTkComboBox(master=dialog_box, values=["9", "10", "11", "12"], variable=grade_level)
    dropdown.pack()

    # Submit grade button
    save_button = ctk.CTkButton(dialog_box, text="Submit", command=save_inputs)
    save_button.place(relx=0.75,rely=0.75,anchor=CENTER)

    save_button = ctk.CTkButton(dialog_box, text="Quit", command=destroyGui)
    save_button.place(relx=0.25,rely=0.75,anchor=CENTER)

def pickWinner():
    print("placeholder")

root = ctk.CTk()
root.geometry("500x350")

Label = ctk.CTkLabel(root, text="Student Involvement Tracker",corner_radius=10)
Label.place(relx= .5, rely=.1, anchor=CENTER)


# BUTTONS

# Allows you to add new students to the database
button1 = ctk.CTkButton(root, text="Add New Student",command=inputStudent, width=350, corner_radius=10)
button1.place(relx= .5, rely=.25, anchor=CENTER)

# Allows you to view all current entries. Returns the complete database in treeview form.
button2 = ctk.CTkButton(root, text="View Entries", command=open_dialog_box, width=350, corner_radius=10)
button2.place(relx= .5, rely=.4, anchor=CENTER)

# Creates a report of the entire database
button5 = ctk.CTkButton(root, text="Pick Winner", command=pickWinner, width=350, corner_radius=10)
button5.place(relx= .5, rely=.55, anchor=CENTER)

# Creates a report of the entire database
button4 = ctk.CTkButton(root, text="Create Report", command=report, width=350, corner_radius=10)
button4.place(relx= .5, rely=.70, anchor=CENTER)

button3 = ctk.CTkButton(root, text="Quit", command=root.destroy, width=350, corner_radius=10)
button3.place(relx= .5, rely=.85, anchor=CENTER)




conn = sqlite3.connect('studentDatabase.db')
cursor = conn.cursor()
# keeps gui running
if __name__ == "__main__":
    root.mainloop()
    cursor.close()
    conn.close()
