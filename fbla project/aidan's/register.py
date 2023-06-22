import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import ImageTk, Image
import pymongo
from pymongo import MongoClient
from tkcalendar import Calendar
from popups import error

cluster = MongoClient("mongodb+srv://RRHSfbla2023:IheBcYm1ZbOEephx@fbla2023project.wdozi9i.mongodb.net/?retryWrites=true&w=majority")
db = cluster["RRHSfbla2023"]
student_info = db["student_info"]
login_info = db["login_info"]

def register():

    event_window = tk.Toplevel()
    event_window.geometry("400x600")
    event_window.configure(bg='#1c1c1c')

    font = ctk.CTkFont(family= "Quicksand", size= 15, weight= "bold")

    def teacher_prompt():
        print(check_var.get())
        if check_var.get() != False:
            prompt = tk.Toplevel()
            prompt.geometry("400x200")
            prompt.configure(bg="#1c1c1c")
            prompt.grab_set()

            label = ctk.CTkLabel(prompt, text= "please enter the confirmation code", font= ("Quicksand", 12))

            password_entry = ctk.CTkEntry(prompt, bg_color= "#1C1F1F", border_width= 0, width= 200, font=("Quicksand", 15), placeholder_text= "last name")
            password_entry.place(relx= .5, rely= .6, anchor= "center")


    username_entry = ctk.CTkEntry(event_window, bg_color= "#1C1F1F", border_width= 0, width= 200, font=("Quicksand", 15), placeholder_text= "first name")
    username_entry.place(relx= .5, rely= .30, anchor= "center")

    password_entry = ctk.CTkEntry(event_window, bg_color= "#1C1F1F", border_width= 0, width= 200, font=("Quicksand", 15), placeholder_text= "last name")
    password_entry.place(relx= .5, rely= .40, anchor= "center")

    grade_level = ctk.IntVar(event_window)
    grade_level.set("select grade")
    grade_options = ctk.CTkComboBox(master=event_window, values=["9", "10", "11", "12"], variable=grade_level, bg_color= "#1C1F1F", border_width= 0, width= 200, font= font)
    grade_options.place(relx= .5, rely= .50, anchor= "center")

    check_var = ctk.BooleanVar(event_window)
    teacherStudent = ctk.CTkCheckBox(master=event_window, text="Teacher",font=("Quicksand", 15), command=teacher_prompt, text_color="white", variable=check_var, onvalue=True, offvalue=False)
    teacherStudent.place(relx=0.5, rely= 0.6, anchor="center")

    sign_in_image = Image.open("./assets/add_new_user.png") # change
    sign_in_image = sign_in_image.resize((270, 75))
    sign_in_image = ImageTk.PhotoImage(sign_in_image)
    sign_in = tk.Label(event_window, image= sign_in_image, bd= 0)
    sign_in.image = sign_in_image
    sign_in.place(relx= .5, rely= .1, anchor= "center")



    def submit():
        username = username_entry.get()
        password = password_entry.get()
        if username == "" or password == "":
            error("please fill out all the required fields")
        else:
            temp = {"username": username, "password": password}
            login_info.insert_one(temp)
            event_window.destroy()

    submit_button = ctk.CTkButton(event_window, text= "submit", font= ("Quicksand", 25), command= submit, bg_color= "#1c1c1c", fg_color= "#1c1c1c", text_color= "white", hover_color= "#292929")
    submit_button.place(relx=0.5, rely=0.85, anchor="center")