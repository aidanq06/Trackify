import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import ImageTk, Image
import pymongo
from pymongo import MongoClient
from tkcalendar import Calendar
from popups import error
from add_student import add_student
import random as rand

cluster = MongoClient("mongodb+srv://RRHSfbla2023:IheBcYm1ZbOEephx@fbla2023project.wdozi9i.mongodb.net/?retryWrites=true&w=majority")
db = cluster["RRHSfbla2023"]
student_info = db["student_info"]
login_info = db["login_info"]
code_info = db["code"]

def register():

    event_window = tk.Toplevel()
    event_window.geometry("400x600")
    event_window.configure(bg='#1c1c1c')

    def teacher_prompt():
        if check_var.get() != False:
            prompt = tk.Toplevel()
            prompt.geometry("400x200")
            prompt.configure(bg="#1c1c1c")
            prompt.grab_set()

            label = ctk.CTkLabel(prompt, text= "enter the administration code", font= ("Quicksand", 20), text_color="white", fg_color="#1c1c1c", bg_color= "#1c1c1c")
            label.place(relx= 0.5, rely= 0.25, anchor= "center")

            password_entry = ctk.CTkEntry(prompt, bg_color= "#1C1F1F", border_width= 0, width= 200, font=("Quicksand", 15), placeholder_text= "enter code here")
            password_entry.place(relx= .5, rely= .5, anchor= "center")

            def submit():
                if check_var.get() == True:
                    code = password_entry.get()
                    if code == "":
                        error("Please fill out all the required fields.")
                    else:
                        codes = code_info.find()
                        for i in codes:
                            if int(code) == i["main"]:
                                prompt.destroy()
                                first_label.configure(text= "username:")
                                second_label.configure(text= "password:")
                                grade_options.place_forget()
                            else:
                                error("Password does not match.")
                else:
                    grade_options.place(relx= .5, rely= .65, anchor= "center")
                    first_label.configure(text= "first name:")
                    second_label.configure(text= "last name:")

            submit_button = ctk.CTkButton(prompt, text= "submit", font= ("Quicksand", 25), command= submit, bg_color= "#1c1c1c", fg_color= "#1c1c1c", text_color= "white", hover_color= "#292929")
            submit_button.place(relx=0.5, rely=0.8, anchor="center")

            def closed():
                check_var.set(False)
                prompt.destroy()
            
            prompt.protocol("WM_DELETE_WINDOW", closed)

    first_label = ctk.CTkLabel(event_window, text= "first name:", font= ("Quicksand", 15), text_color="white", fg_color="#1c1c1c", bg_color= "#1c1c1c")
    first_label.place(relx= 0.5, rely= 0.25, anchor= "center")

    username_entry = ctk.CTkEntry(event_window, bg_color= "#1C1F1F", border_width= 0, width= 200, font=("Quicksand", 15))
    username_entry.place(relx= 0.5, rely= 0.3, anchor= "center")

    second_label = ctk.CTkLabel(event_window, text= "last name:", font= ("Quicksand", 15), text_color="white", fg_color="#1c1c1c", bg_color= "#1c1c1c")
    second_label.place(relx= 0.5, rely= 0.4, anchor= "center")

    password_entry = ctk.CTkEntry(event_window, bg_color= "#1C1F1F", border_width= 0, width= 200, font=("Quicksand", 15))
    password_entry.place(relx= 0.5, rely= 0.45, anchor= "center")

    grade_level = ctk.IntVar(event_window)
    grade_level.set("select grade")
    grade_options = ctk.CTkComboBox(master=event_window, values=["9", "10", "11", "12"], variable=grade_level, bg_color= "#1C1F1F", border_width= 0, width= 200, font= ("Quicksand", 15))
    grade_options.place(relx= 0.5, rely= 0.65, anchor= "center")

    check_var = ctk.BooleanVar(event_window)
    teacherStudent = ctk.CTkCheckBox(master=event_window, text="Teacher",font=("Quicksand", 15), command=teacher_prompt, text_color="white", variable=check_var, onvalue=True, offvalue=False)
    teacherStudent.place(relx=0.5, rely= 0.75, anchor="center")

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
            if check_var.get() == True:
                temp = {"username": username, "password": password}
                login_info.insert_one(temp)
                event_window.destroy()

            else:
                students = student_info.find()
                studentId = 0
                studentId = rand.randint(0,100000)
                check_dup = 0
                while check_dup == 0:
                    for student in students:
                        if int(student["_id"]) == int(studentId):
                            studentId = rand.randint(0,100000)
                            break
                    check_dup = 1
                grade = int(grade_options.get())
                temp = {"_id": studentId, "first_name": username, "last_name": password, "grade":grade, "point": 0}
                student_info.insert_one(temp)

                root = tk.Toplevel()
                root.geometry("400x100")
                root.configure(bg= "#1c1c1c")
                label= ctk.CTkLabel(root, text= f'your student id and password is: {studentId}', font= ("Quicksand", 18), bg_color= '#1c1c1c', fg_color= '#1c1c1c', text_color= "white")
                label.place(relx= 0.5, rely= 0.5, anchor= "center")

            # Define a function to close both windows
        def close_both_windows():
            event_window.destroy()
            root.destroy()

        # Call close_both_windows when the new_window's close button is clicked
        root.protocol("WM_DELETE_WINDOW", close_both_windows)

            

    submit_button = ctk.CTkButton(event_window, text= "submit", font= ("Quicksand", 25), command= submit, bg_color= "#1c1c1c", fg_color= "#1c1c1c", text_color= "white", hover_color= "#292929")
    submit_button.place(relx=0.5, rely=0.9, anchor="center")