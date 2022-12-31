# Import the required modules
import sqlite3
from tkinter import *
import tkinter as tk

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
2. Attended River Ridge dance
3. Attended River Ridge pep rally
4. Attended River Ridge homecoming
5. Attended River Ridge photoshoot
ideas:spelling bee, rrhs musical

1. Attended River Ridge soccer games
2. Attended River Ridge football games
3. Attended River Ridge lacross games
4. Attended River Ridge basketball
5. Attended River Ridge volleyball
"""
#create a student class with the attributes "first" "last" and "grade" correlating to the students first and last name as well as the students grade
class student():
    def __init__(self, first, last, grade):
        self.first = first
        self.last = last
        self.grade = grade

def error():
    ...

def open_dialog_box():
    # Create a new top-level window (i.e., a new window that is independent of the main window)
    dialog_box = tk.Toplevel()
    dialog_box.title("Dialog Box")

    # Create a list of options
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE grade = 12 OR 11 OR 10 OR 9 OR 8 OR 7 OR 6")
    options = cursor.fetchall()
    

    # Create a variable to store the selected options
    selected_options = tk.StringVar(value=options)

    # Create a listbox widget to display the options
    listbox = tk.Listbox(dialog_box, selectmode="multiple", listvariable=selected_options)
    for option in options:
        listbox.insert("end", option)
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

    # Add a "Save" button to the dialog box
    save_button = tk.Button(dialog_box, text="Save", command=save_selection)
    save_button.pack()


    
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
    # Define a function to be called when the "Save" button is clicked
    def save_inputs():
        # Get the values entered in the entry widgets
        try:
            print(entry1.get())
            print(entry2.get())
            print(grade_level.get())
            new_student = student(entry1.get(), entry2.get(), grade_level.get())
        except ValueError:
            ...
            # do a pop up window telling them its a value error


        # database init
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
#        cursor.execute("""CREATE TABLE students (
#                            first text,
#                            last text,
#                            grade integer
#                            )""")

        # Save the values to database
        cursor.execute("INSERT INTO students VALUES (?, ?, ?)", (new_student.first, new_student.last, new_student.grade))
        
        conn.commit()
        conn.close()

        # Close the input window
        inputStudent.destroy()

    # Add a "Save" button to the input window
    save_button = tk.Button(inputStudent, text="Submit", command=save_inputs)
    save_button.pack()

root = tk.Tk()

tk.Label(root, text="FBLA Project").grid(column=0, row=0)

# BUTTONS
tk.Button(root, text="Add New Student", command=inputStudent).grid(column=1, row=0)
tk.Button(root, text="Quit", command=root.destroy).grid(column=1, row=2)
tk.Button(root, text="Open Dialog Box", command=open_dialog_box).grid(column=1,row=1)
# keeps gui running
if __name__ == "__main__":
    root.mainloop()