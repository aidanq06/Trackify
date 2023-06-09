import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import ImageTk, Image
import pymongo
from pymongo import MongoClient
import random as rand

cluster = MongoClient("mongodb+srv://RRHSfbla2023:IheBcYm1ZbOEephx@fbla2023project.wdozi9i.mongodb.net/?retryWrites=true&w=majority")
db = cluster["RRHSfbla2023"]
student_info = db["student_info"]


def add_student():
    add_window = tk.Toplevel()
    add_window.geometry("600x600")
    add_window.configure(bg='#1c1c1c')

    style = ttk.Style(add_window)
    style.theme_use('clam')

    font = ctk.CTkFont(family= "Quicksand", size= 15, weight= "bold")

    student_first_entry = ctk.CTkEntry(add_window, bg_color= "#1C1F1F", border_width= 0, width= 200, font= font, placeholder_text= "enter first name")
    student_first_entry.place(relx= .5, rely= .3, anchor= "center")

    student_last_entry = ctk.CTkEntry(add_window, bg_color= "#1C1F1F", border_width= 0, width= 200, font= font, placeholder_text= "enter last name")
    student_last_entry.place(relx= .5, rely= .45, anchor= "center")

    grade_level = ctk.IntVar(add_window)
    grade_level.set("select grade")
    grade_options = ctk.CTkComboBox(master=add_window, values=["9", "10", "11", "12"], variable=grade_level, bg_color= "#1C1F1F", border_width= 0, width= 200, font= font)
    grade_options.place(relx= .5, rely= .6, anchor= "center")

    sign_in_image = Image.open("./assets/add_new_event.png")
    sign_in_image = sign_in_image.resize((270, 75))
    sign_in_image = ImageTk.PhotoImage(sign_in_image)
    sign_in = tk.Label(add_window, image= sign_in_image, bd= 0)
    sign_in.image = sign_in_image
    sign_in.place(relx= .5, rely= .1, anchor= "center")



    def submit():
        student_first = student_first_entry.get()
        student_last = student_last_entry.get()
        student_temp = student_info.find()
        grade = grade_level.get()
        studentId = 0
        studentId = rand.randint(0,100000)
        check_dup = 0
        
        if student_first == "" or student_last == "" or grade == "":
            ...
        else:
            while check_dup == 0:
                for students in student_temp:
                    if int(students.get('_id')) == int(studentId):
                        studentId = rand.randint(0,100000)
                        break
                        
                check_dup == 1
                temp = {"first_name": student_first, "last_name": student_last, "grade": int(grade), "_id": studentId, "point": 0}
                student_info.insert_one(temp)
                add_window.destroy()
        

    submit_image = Image.open("./assets/submit.png")
    submit_image = submit_image.resize((100, 60))
    submit_image = ImageTk.PhotoImage(submit_image)
    submit_button = tk.Button(add_window, image= submit_image, command= submit, bd= 0)
    submit_button.image = submit_image
    submit_button.place(relx=0.5, rely=0.85, anchor="center")
