import customtkinter as ctk
from tkinter import *
import random as rand
import tkinter as tk

from popups import success, error
from main import connect_to_db

cursor = connect_to_db()

class student():
    def __init__(self, first, last, grade, number):
        self.first = first
        self.last = last
        self.grade = grade
        self.number = number

def inputStudent(self):

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

                # Close the input window
                inputStudent.destroy()
                success(f"Successfully added {student_first} {student_last} ({grade_level.get()}) to the database.")

        except:
            error("Please fill in all fields!")

    # Add a "Save" button to the input window
    save_button = ctk.CTkButton(inputStudent, text="Submit", command=save_inputs)
    save_button.place(relx= .15, rely=0.85)

