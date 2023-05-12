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
    event_window = tk.Toplevel()
    event_window.geometry("600x600")
    event_window.configure(bg='#1c1c1c')

    style = ttk.Style(event_window)
    style.theme_use('clam')

    font = ctk.CTkFont(family= "Quicksand", size= 15, weight= "bold")

    student_first_entry = ctk.CTkEntry(event_window, bg_color= "#1C1F1F", border_width= 0, width= 200, font= font, placeholder_text= "enter first name")
    student_first_entry.place(relx= .5, rely= .3, anchor= "center")

    student_last_entry = ctk.CTkEntry(event_window, bg_color= "#1C1F1F", border_width= 0, width= 200, font= font, placeholder_text= "enter last name")
    student_last_entry.place(relx= .5, rely= .45, anchor= "center")

    grade_entry = ctk.CTkEntry(event_window, bg_color= "#1C1F1F", border_width= 0, width= 200, font= font, placeholder_text= "enter grade")
    grade_entry.place(relx= .5, rely= .6, anchor= "center")

    sign_in_image = Image.open("./assets/add_new_event.png")
    sign_in_image = sign_in_image.resize((270, 75))
    sign_in_image = ImageTk.PhotoImage(sign_in_image)
    sign_in = tk.Label(event_window, image= sign_in_image, bd= 0)
    sign_in.image = sign_in_image
    sign_in.place(relx= .5, rely= .1, anchor= "center")



    def submit():
        student_first = student_first_entry.get()
        student_last = student_last_entry.get()
        student_temp = student_info.find()
        grade = grade_entry.get()
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
                temp = {"first_name": student_first, "last_name": student_last, "grade": int(grade), "_id": studentId}
                student_info.insert_one(temp)
                event_window.destroy()
        

    submit_image = Image.open("./assets/submit.png")
    submit_image = submit_image.resize((100, 60))
    submit_image = ImageTk.PhotoImage(submit_image)
    submit_button = tk.Button(event_window, image= submit_image, command= submit, bd= 0)
    submit_button.image = submit_image
    submit_button.place(relx=0.5, rely=0.85, anchor="center")
