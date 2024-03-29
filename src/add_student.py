import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import ImageTk, Image
from pymongo import MongoClient
import random as rand
from popups import error

cluster = MongoClient("mongodb+srv://RRHSfbla2023:IheBcYm1ZbOEephx@fbla2023project.wdozi9i.mongodb.net/?retryWrites=true&w=majority")
db = cluster["RRHSfbla2023"]
student_info = db["student_info"]


def add_student(root):

    add_window = tk.Frame(root, height= 500, width= 1000, bg= "#1c1c1c")
    add_window.place(relx= 0, rely= 0, anchor= "nw")

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

    sign_in = ctk.CTkLabel(add_window, text= "add a new student", font= ("Quicksand", 25), bg_color= '#1c1c1c', fg_color= '#1c1c1c', text_color= "white")
    sign_in.place(relx= .5, rely= .1, anchor= "center")



    def submit():
        student_first = student_first_entry.get()
        student_last = student_last_entry.get()
        student_temp = student_info.find()
        try:
            grade = grade_level.get()
        except:
            error("Please fill out all required fields.")
        studentId = 0
        studentId = rand.randint(0,100000)
        check_dup = 0
        
        if student_first == "" or student_last == "" or grade == "":
            error("Please fill out all the required fields.")
        else:
            while check_dup == 0:
                for students in student_temp:
                    if int(students["_id"]) == int(studentId):
                        studentId = rand.randint(0,100000)
                        break
                        
                check_dup = 1
            temp = {"_id": studentId, "first_name": student_first, "last_name": student_last, "grade": int(grade), "point": 0}
            student_info.insert_one(temp)
            add_window.destroy()
        

    submit_button = ctk.CTkButton(add_window, text= "submit", font= ("Quicksand", 25), bg_color= '#1c1c1c', fg_color= '#1c1c1c', text_color= "white", command= submit, hover_color="#292929")
    submit_button.place(relx=0.5, rely=0.85, anchor="center")

    back_image = Image.open("./assets/back.png")
    back_image = back_image.resize((50, 40))
    back_image = ImageTk.PhotoImage(back_image)   
    back_button = tk.Button(add_window, image=back_image, border = 0, highlightthickness = 0, command= add_window.destroy)
    back_button.image = back_image
    back_button.place(relx=0.075, rely=0.075, anchor="center")