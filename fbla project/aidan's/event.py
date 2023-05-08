import tkinter as tk
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

    font = ctk.CTkFont(family= "Quicksand", size= 15, weight= "bold")

    event_type_entry = ctk.CTkEntry(event_window, bg_color= "#1C1F1F", border_width= 0, width= 200, font= font, placeholder_text= "event name")
    event_type_entry.place(relx= .5, rely= .3, anchor= "center")

    tkc = Calendar(event_window, selectmode= "day", year= 2023, month= 1, date= 1,background="#1c1c1c", disabledbackground="#1c1c1c", bordercolor="#1c1c1c", 
               headersbackground="#1c1c1c", normalbackground="#1c1c1c", foreground='white', 
               normalforeground='white', headersforeground='white')
    tkc.config(background= '#1c1c1c')
    tkc.place(relx= .5, rely= .4, anchor= "n")

    sign_in_image = Image.open("./assets/add_new_event.png")
    sign_in_image = sign_in_image.resize((270, 75))
    sign_in_image = ImageTk.PhotoImage(sign_in_image)
    sign_in = tk.Label(event_window, image= sign_in_image, bd= 0)
    sign_in.image = sign_in_image
    sign_in.place(relx= .5, rely= .1, anchor= "center")



    def submit():
        event_type = event_type_entry.get()
        event_date = tkc.get_date()
        if event_type == "" or event_date == "":
            ...
        else:
            temp = {"name": event_type, "date": event_date}
            event_info.insert_one(temp)
            event_window.destroy()
        

    submit_image = Image.open("./assets/submit.png")
    submit_image = submit_image.resize((100, 60))
    submit_image = ImageTk.PhotoImage(submit_image)
    submit_button = tk.Button(event_window, image=submit_image, command= submit, bd= 0)
    submit_button.image = submit_image
    submit_button.place(relx=0.5, rely=0.8, anchor="center")

