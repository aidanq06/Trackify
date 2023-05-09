import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import ImageTk, Image
import pymongo
from pymongo import MongoClient
from tkcalendar import Calendar

cluster = MongoClient("mongodb+srv://RRHSfbla2023:IheBcYm1ZbOEephx@fbla2023project.wdozi9i.mongodb.net/?retryWrites=true&w=majority")
db = cluster["RRHSfbla2023"]
student_info = db["student_info"]
event_info = db["event_info"]


def register():
    event_window = tk.Toplevel()
    event_window.geometry("600x600")
    event_window.configure(bg='#1c1c1c')

    style = ttk.Style(event_window)
    style.theme_use('clam')

    font = ctk.CTkFont(family= "Quicksand", size= 15, weight= "bold")

    event_type_entry = ctk.CTkEntry(event_window, bg_color= "#1C1F1F", border_width= 0, width= 200, font= font, placeholder_text= "event name")
    event_type_entry.place(relx= .5, rely= .15, anchor= "center")

    firstname = ctk.CTkEntry(event_window, bg_color= "#1C1F1F", border_width= 0, width= 200, font= font, placeholder_text= "firstname")
    firstname.place(relx= .5, rely= .30, anchor= "center")

    lastname = ctk.CTkEntry(event_window, bg_color= "#1C1F1F", border_width= 0, width= 200, font= font, placeholder_text= "lastname")
    lastname.place(relx= .5, rely= .40, anchor= "center")

    grade = ctk.CTkEntry(event_window, bg_color= "#1C1F1F", border_width= 0, width= 200, font= font, placeholder_text= "grade")
    grade.place(relx= .5, rely= .50, anchor= "center")

    sign_in_image = Image.open("./assets/add_new_event.png") # change
    sign_in_image = sign_in_image.resize((270, 75))
    sign_in_image = ImageTk.PhotoImage(sign_in_image)
    sign_in = tk.Label(event_window, image= sign_in_image, bd= 0)
    sign_in.image = sign_in_image
    sign_in.place(relx= .5, rely= .1, anchor= "center")



    def submit():
        event_type = event_type_entry.get()
        point_value = firstname.get()
        if event_type == "" or point_value == "":
            ...
        else:
            temp = {"name": event_type, "points": int(point_value)}
            event_info.insert_one(temp)
            event_window.destroy()
        

    submit_image = Image.open("./assets/submit.png")
    submit_image = submit_image.resize((100, 60))
    submit_image = ImageTk.PhotoImage(submit_image)
    submit_button = tk.Button(event_window, image=submit_image, command= submit, bd= 0)
    submit_button.image = submit_image
    submit_button.place(relx=0.5, rely=0.85, anchor="center")