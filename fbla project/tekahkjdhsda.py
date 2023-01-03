# Import the required modules
import sqlite3
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import random as rand


"""
# Connect to the database
conn = sqlite3.connect('mydatabase.db')
# Create a cursor
cursor = conn.cursor()
# Create the table
cursor.execute('''CREATE TABLE students (name TEXT, lastname TEXT, grade INTEGER, points INTEGER)''')
# Commit the changes to the database
conn.commit()
# Close the connection to the database
conn.close()
"""

"""
Must have at least five sporting events and five non-sports school events.
1. Attended River Ridge prom
2. Attended River Ridge dance performance
3. Attended River Ridge pep rally
4. Attended River Ridge homecoming
5. Attended River Ridge musical
ideas:spelling bee

1. Attended River Ridge soccer games
2. Attended River Ridge football games
3. Attended River Ridge lacross games
4. Attended River Ridge basketball
5. Attended River Ridge volleyball
"""
global student_number
#create a student class with the attributes "first" "last" and "grade" correlating to the students first and last name as well as the students grade
class student():
    def __init__(self, first, last, grade, number):
        self.first = first
        self.last = last
        self.grade = grade
        self.number = number

def error():
    ...

def open_dialog_box():
    # Create a new top-level window (i.e., a new window that is independent of the main window)
    dialog_box = tk.Toplevel()
    dialog_box.title("Dialog Box")

    # Create a list of students
    cursor.execute("SELECT * FROM students WHERE grade = 12 OR 11 OR 10 OR 9 OR 8 OR 7 OR 6")
    options = cursor.fetchall()

    # Create a variable to store the selected options
    selected_options = tk.StringVar(value=options)

    # Create a listbox widget to display the options
    listbox = ttk.Treeview(dialog_box, selectmode="extended",columns=("c1", "c2", "c3", "c4"),show="headings" )
    listbox.column("# 1", anchor=CENTER)
    listbox.heading("# 1", text="first name")
    listbox.column("# 2", anchor=CENTER)
    listbox.heading("# 2", text="last name")
    listbox.column("# 3", anchor=CENTER)
    listbox.heading("# 3", text="grade")
    listbox.column("# 4", anchor=CENTER)
    listbox.heading("# 4", text="points")
    for option in options:
        listbox.insert('', 'end', values=(option))
    listbox.pack()

    # Define a function to be called when the "Save" button is clicked
    def save_selection():
        # Get the selected options
        selection = listbox.curselection()
        selected_values = [options[index] for index in selection]

        # Save the selected options to a variable (in this case, a global variable)
        global var
        var = selected_values

        # Close the dialog box
        dialog_box.destroy()

    #create a function to remove one or more students using selection
    def remove_student():
        items = listbox.selection()
        for i in items:
            selection = listbox.item(i, option="values")
            temp_name = selection[1]
            temp_name2 = selection[0]
            student_number = selection[4]
            cursor.execute("DELETE FROM students WHERE first = :first AND last = :last AND number = :studentnumber",{'first': temp_name2, 'last': temp_name, 'studentnumber': student_number})
        conn.commit()

        # Close the dialog box
        dialog_box.destroy()

    #creates a function to remove all students
    def remove_everyone():
        cursor.execute("DELETE FROM students")
        conn.commit()

        dialog_box.destroy()

    def add_points():
        def get_value():
            try:
                point_value = e1.get()
                print(point_value)
                cursor.execute("UPDATE students SET points = :point WHERE first = :first AND last = :last AND number = :number", {'point': point_value, 'first': temp_name2, 'last': temp_name, 'number': number })
                conn.commit()
            except ValueError:
                ...
            new_points.destroy()
            dialog_box.destroy()
        try:
            items = listbox.selection()
            selection = listbox.item(items, option="values")
            temp_name = selection[1]
            temp_name2 = selection[0]
            number = selection[4]
        except ValueError:
            ...
        new_points= tk.Toplevel()
        new_points.title("add points to student")
        l1 = tk.Label(new_points, text= "Please enter the points you would like to assign " + temp_name2 + " " + temp_name)
        l1.pack()
        e1 = tk.Entry(new_points)
        e1.pack()
        submit = tk.Button(new_points, text="submit", command= get_value)
        submit.pack()


    # Add a "Save" button to the dialog box
    save_button = tk.Button(dialog_box, text="Save", command=save_selection)
    save_button.pack()

    # Add a "remove student" button to the dialog box
    remove_button = tk.Button(dialog_box, text="Remove student", command= remove_student)
    remove_button.pack()

    # add a "remove all" button to the dialog box
    remove_all = tk.Button(dialog_box, text="Remove all", command= remove_everyone)
    remove_all.pack()

    add_points_button = tk.Button(dialog_box, text= "Edit student points", command= add_points)
    add_points_button.pack()
    
def inputStudent():

    # Create a new top-level window (i.e., a new window that is independent of the main window)
    inputStudent = tk.Toplevel()
    inputStudent.title("Enter New Student")

    # Add three labels and three entry widgets to the input window
    label1 = tk.Label(inputStudent, text="Enter the student's name.")
    label1.pack()
    entry1 = tk.Entry(inputStudent)
    entry1.pack()

    label2 = tk.Label(inputStudent, text="Enter the student's last name.")
    label2.pack()
    entry2 = tk.Entry(inputStudent)
    entry2.pack()

    label3 = tk.Label(inputStudent, text="Select the student's grade")
    label3.pack()
    grade_level = IntVar(inputStudent)
    grade_level.set("Select a grade")
    entry3 = OptionMenu(inputStudent, grade_level, 6, 7, 8, 9, 10, 11, 12)
    entry3.pack()

    var1 = tk.IntVar()
    var1.set(1)
    cb = tk.Checkbutton(inputStudent, text= "ignore duplicate students", variable= var1)
    cb.pack()

    # Define a function to be called when the "Save" button is clicked
    def save_inputs():
        # generate a random student id
        var2 = tk.IntVar()
        var2.set(rand.randint(0,100000))
        # Get the values entered in the entry widgets
        try:
#            new_student = student(entry1.get(), entry2.get(), grade_level.get())
            new_student = student(entry1.get(), entry2.get(), grade_level.get(), var2)
        except ValueError:
            ...
            # do a pop up window telling them its a value error


        # database init
#        cursor.execute("""CREATE TABLE students (
#                            first text,
#                            last text,
#                            grade integer,
#                            points integer,
#                            number integer
#                            )""")

        # Save the values to database
        cursor.execute("SELECT * FROM students WHERE grade = 12 OR 11 OR 10 OR 9 OR 8 OR 7 OR 6")
        options =cursor.fetchall()
        student_first = new_student.first.capitalize()
        student_last = new_student.last.capitalize()
        if var1.get() == 0 or len(options) == 0:
            cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?)", (student_first, student_last, new_student.grade, 0, var2.get()))
        else:
            for option in range(len(options)):
                if options[option][4] == var2.get():
                    var2.set(rand.randint(0, 100000))
                if not(new_student.first == options[option][0] and new_student.last == options[option][1] and new_student.grade == options[option][2]):
                    cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?)", (student_first, student_last, new_student.grade, 0, var2.get()))
                else:
                    ...
        conn.commit()


        # Close the input window
        inputStudent.destroy()


    # Add a "Save" button to the input window
    save_button = tk.Button(inputStudent, text="Submit", command=save_inputs)
    save_button.pack()

root = tk.Tk()
root.geometry("400x200")

tk.Label(root, text="FBLA Project").grid(column=0, row=0)

# BUTTONS
tk.Button(root, text="Add New Student",command=inputStudent, width=56).grid(column=0, row=1)
tk.Button(root, text="Quit", command=root.destroy, width=56).grid(column=0, row=5)
tk.Button(root, text="View/Edit Students", command=open_dialog_box, width=56).grid(column=0,row=3)
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
# keeps gui running
if __name__ == "__main__":
    root.mainloop()
cursor.close()
conn.close()