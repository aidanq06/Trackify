import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import random as rand
from PIL import ImageTk, Image
import pymongo
from pymongo import MongoClient
import datetime
import random
from tkextrafont import Font
from popups import error

cluster = MongoClient("mongodb+srv://RRHSfbla2023:IheBcYm1ZbOEephx@fbla2023project.wdozi9i.mongodb.net/?retryWrites=true&w=majority")
db = cluster["RRHSfbla2023"]
student_info = db["student_info"]
event_info = db["event_info"]
login_info = db["login_info"]
request_info = db["request_info"]

def view_entries():

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", fieldbackground= "#1c1c1c", background = "#1c1c1c", foreground= "white", font= ("Quicksand", 12), rowheight= 80, highlightbackground = "#1c1c1c", highlightcolor= "#1c1c1c")
    style.configure("Treeview.Heading", background = "#1c1c1c", foreground= "white", borderwidth= 0, font= ("Quicksand", 12))

    root1 = tk.Toplevel()
    root1.geometry("1000x500")
    root1.configure(bg= '#1c1c1c')
    students = student_info.find()

    listbox = ttk.Treeview(root1, selectmode="extended",columns=("c1", "c2", "c3", "c4", "c5"),show="headings", height= 5)
    listbox.column("# 1", anchor=CENTER, width = 199)
    listbox.heading("# 1", text="Student id")
    listbox.column("# 2", anchor=CENTER, width = 199)
    listbox.heading("# 2", text="First Name")
    listbox.column("# 3", anchor=CENTER, width = 199)
    listbox.heading("# 3", text="Last Name")
    listbox.column("# 4", anchor=CENTER, width = 199)
    listbox.heading("# 4", text="Grade Level")
    listbox.column("# 5", anchor=CENTER, width = 199)
    listbox.heading("# 5", text="Points")



    def refresh():
        for item in listbox.get_children():
            listbox.delete(item)
        students= student_info.find()
        student_list = list()
        count = 0
        for student in students:
            student_list.append(student)
        student_list.reverse()
        for student in student_list:
            listbox.insert(parent='', index='end', text= "", iid= count, values= (student["_id"], student["first_name"], student["last_name"], student["grade"], student["point"]) )
            count+= 1
        listbox.place(relx= 0, rely= 0, anchor= "nw")

    refresh()

    def remove_student():
        selection = list()
        items = listbox.selection()
        for item in items:
            selection.append(listbox.item(item, option="values"))
        if len(selection) != 0:
            temp = student_info.find()
            for select in selection:
                for student in temp:
                    if int(student["_id"]) == int(select[0]):
                        student_info.delete_one({"_id": student["_id"]})
                        break
        else:
            error("Please select one or more students to remove.")
        refresh()

    def edit_student():
        item = listbox.selection()
        try:
            selection = listbox.item(item, option="values")

            if len(selection) == 0:
                error("Please select a student to edit.")
            else:
                edit_student_window = tk.Toplevel()
                edit_student_window.geometry("400x600")
                edit_student_window.configure(bg= '#1c1c1c')

                label = ctk.CTkLabel(edit_student_window, text= "edit student", font= ("Quicksand", 25), bg_color= '#1c1c1c', fg_color= '#1c1c1c', text_color= "white")
                label.place(relx= 0.5, rely= 0.1, anchor= "center")

                first_entry = ctk.CTkEntry(edit_student_window, bg_color= "#1C1C1C", border_width= 0, width= 200, font= ("Quicksand", 15))
                first_entry.insert(0, selection[1])
                def first_select(event):
                    first_entry.select_range(0, END)
                first_entry.bind("<FocusIn>", first_select)
                first_entry.place(relx= 0.5, rely= 0.2, anchor= "center")

                last_entry = ctk.CTkEntry(edit_student_window, bg_color= "#1C1F1F", border_width= 0, width= 200, font= ("Quicksand", 15))
                last_entry.insert(0, selection[2])
                def last_select(event):
                    last_entry.select_range(0, END)
                last_entry.bind("<FocusIn>", last_select)
                last_entry.place(relx= 0.5, rely= 0.4, anchor= "center")

                grade_entry = ctk.CTkEntry(edit_student_window, bg_color= "#1C1F1F", border_width= 0, width= 200, font= ("Quicksand", 15))
                grade_entry.insert(0, selection[3])
                def grade_select(event):
                    grade_entry.select_range(0, END)
                grade_entry.bind("<FocusIn>", grade_select)
                grade_entry.place(relx= 0.5, rely= 0.6, anchor= "center")

                def get_submit():
                    first= first_entry.get()
                    last= last_entry.get()
                    grade= grade_entry.get()

                    if first == "" or last == "" or grade == "":
                        error("Please fill out all the required fields.")

                    try:
                        grade = int(grade)
                    except:
                        error("Grade must be an integer value.")

                    if grade > 12 or grade < 9:
                        error("Grade must be in between 9 and 12.")
                    else:
                        student_info.update_one({"_id": int(selection[0])}, {"$set":{"first_name": str(first).capitalize(), "last_name": (str(last).capitalize()), "grade": int(grade)}})
                        refresh()
                        edit_student_window.destroy()

                submit_button = ctk.CTkButton(edit_student_window, text= "submit", font= ("Quicksand", 20), command= get_submit, bg_color= "#1c1c1c", fg_color= "#1c1c1c", text_color= "white", hover_color="#292929")
                submit_button.place(relx= 0.5, rely= 0.8, anchor= "center")

        except:
            error("You can only edit one student at a time.")

    
    edit_button = ctk.CTkButton(root1, text= "edit student", font= ("Quicksand", 25), bg_color= '#1c1c1c', fg_color= '#1c1c1c', text_color= "white", command= edit_student, hover_color="#292929")
    edit_button.place(relx= 0.15, rely= 0.885, anchor= "nw")

    remove_button = ctk.CTkButton(root1, text= "remove student", font= ("Quicksand", 25), bg_color= '#1c1c1c', fg_color= '#1c1c1c', text_color= "white", command= remove_student, hover_color="#292929")
    remove_button.place(relx= 0.5, rely= 0.885, anchor= "n")

    quit_button = ctk.CTkButton(root1, text= "close", font= ("Quicksand", 25), bg_color= '#1c1c1c', fg_color= '#1c1c1c', text_color= "white", command= root1.destroy, hover_color="#292929")
    quit_button.place(relx= 0.85, rely= 0.885, anchor= "ne")

        