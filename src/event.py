import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import ImageTk, Image
import pymongo
from pymongo import MongoClient
from tkcalendar import Calendar
from popups import error

import datetime

cluster = MongoClient("mongodb+srv://RRHSfbla2023:IheBcYm1ZbOEephx@fbla2023project.wdozi9i.mongodb.net/?retryWrites=true&w=majority")
db = cluster["RRHSfbla2023"]
student_info = db["student_info"]
event_info = db["event_info"]

def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)

def add_event(root):

    event_window = tk.Frame(root, height= 500, width= 1000, bg= "#1c1c1c")
    event_window.place(relx= 0, rely= 0, anchor= "nw")

    style = ttk.Style(event_window)
    style.theme_use('clam')

    font = ctk.CTkFont(family= "Quicksand", size= 15, weight= "bold")


    today=datetime.date.today()
    tkc = Calendar(event_window, selectmode="day", font="Quicksand 15", background="#1c1c1c",
                disabledbackground="#1c1c1c", bordercolor="#1c1c1c", headersbackground="#1c1c1c",
                normalbackground="#1c1c1c", foreground='#1c1c1c', normalforeground='white', headersforeground='white',
                showweeknumbers=False, weekendbackground="#1c1c1c", weekendforeground='white', showothermonthdays=True,
                othermonthforeground='gray', othermonthbackground='#1c1c1c', othermonthwebackground='#1c1c1c',year=today.year,month=today.month)
    tkc.config(background='white')
    tkc.place(relx=.5, rely=.3, anchor="n")


    sign_in_image = Image.open("./assets/add_new_event.png")
    sign_in_image = sign_in_image.resize((270, 75))
    sign_in_image = ImageTk.PhotoImage(sign_in_image)
    sign_in = tk.Label(event_window, image= sign_in_image, bd= 0)
    sign_in.image = sign_in_image
    sign_in.place(relx= .5, rely= .1, anchor= "center")

    event_type_entry = ctk.CTkEntry(event_window, bg_color= "#1C1F1F", border_width= 0, width= 350, font= font, placeholder_text= "event name")
    event_type_entry.place(relx= .3, rely= .2, anchor= "center")

    points_text = ctk.StringVar(value="select initial points")  # set initial value
    event_points_entry = ctk.CTkComboBox(event_window, values=["10","15","20","25"], command=combobox_callback, variable=points_text,border_width= 0, width= 350, font= font) # 
    event_points_entry.place(relx= .7, rely= .2, anchor= "center")

    def submit():
        event_type = event_type_entry.get()
        event_date = tkc.get_date()
        event_points = event_points_entry.get()
        if event_type == "" or event_date == "" or event_points == "":
            error("Please fill out all the required fields.")
        else:
            temp = {"name": event_type, "date": event_date, "points": int(event_points)}
            event_info.insert_one(temp)
            event_window.destroy()
        

    submit_button = ctk.CTkButton(event_window, text= "submit", font= ("Quicksand", 20), bg_color= '#1c1c1c', fg_color= 'white', text_color= "#1c1c1c", command= submit, hover_color="#292929", height=40, width=250)
    submit_button.place(relx=0.5, rely=0.94, anchor="center")
