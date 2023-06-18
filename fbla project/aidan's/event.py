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


def event():
    event_window = tk.Toplevel()
    event_window.geometry("600x600")
    event_window.configure(bg='#1c1c1c')

    style = ttk.Style(event_window)
    style.theme_use('clam')

    font = ctk.CTkFont(family= "Quicksand", size= 15, weight= "bold")

    event_type_entry = ctk.CTkEntry(event_window, bg_color= "#1C1F1F", border_width= 0, width= 200, font= font, placeholder_text= "event name")
    event_type_entry.place(relx= .25, rely= .25, anchor= "center")

    event_points_entry = ctk.CTkEntry(event_window, bg_color= "#1C1F1F", border_width= 0, width= 200, font= font, placeholder_text= "event point value")
    event_points_entry.place(relx= .75, rely= .25, anchor= "center")

    tkc = Calendar(event_window, selectmode= "day", year= 2023, month= 1, date= 1, font= "Quicksand 15", background="#1c1c1c", disabledbackground="#1c1c1c", bordercolor="#1c1c1c", 
               headersbackground="#1c1c1c", normalbackground="#1c1c1c", foreground='white', 
               normalforeground='white', headersforeground='white', date_pattern= "mm/dd/yyyy")
    tkc.config(background= '#1c1c1c')
    tkc.place(relx= .5, rely= .35, anchor= "n")

    sign_in_image = Image.open("./assets/add_new_event.png")
    sign_in_image = sign_in_image.resize((270, 75))
    sign_in_image = ImageTk.PhotoImage(sign_in_image)
    sign_in = tk.Label(event_window, image= sign_in_image, bd= 0)
    sign_in.image = sign_in_image
    sign_in.place(relx= .5, rely= .1, anchor= "center")



    def submit():
        event_type = event_type_entry.get()
        event_date = tkc.get_date()
        point_value = event_points_entry.get()
        if event_type == "" or event_date == "" or point_value == "":
            ...
        else:
            temp = {"name": event_type, "date": event_date, "points": int(point_value)}
            event_info.insert_one(temp)
            event_window.destroy()
        

    submit_image = Image.open("./assets/submit.png")
    submit_image = submit_image.resize((100, 60))
    submit_image = ImageTk.PhotoImage(submit_image)
    submit_button = tk.Button(event_window, image=submit_image, command= submit, bd= 0)
    submit_button.image = submit_image
    submit_button.place(relx=0.5, rely=0.85, anchor="center")

