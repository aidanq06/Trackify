from tkinter import *
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import random as rand
from PIL import ImageTk, Image
import pymongo
from pymongo import MongoClient
import datetime

cluster = MongoClient("mongodb+srv://RRHSfbla2023:IheBcYm1ZbOEephx@fbla2023project.wdozi9i.mongodb.net/?retryWrites=true&w=majority")
db = cluster["RRHSfbla2023"]
student_info = db["student_info"]
event_info = db["event_info"]
login_info = db["login_info"]
request_info = db["request_info"]


def view_requests():
    root1 = tk.Toplevel()
    root1.geometry("800x400")
    root1.configure(bg= '#1c1c1c')
    requests = request_info.find()
    names = list()
    id1 = list()
    temp = list()
    id2 = list()
    first = list()
    last = list()
    students = student_info.find()

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", fieldbackground= "#1c1c1c", background = "#1c1c1c", foreground= "white", font= ("none", 10), rowheight= 40, highlightbackground = "#1c1c1c", highlightcolor= "#1c1c1c")
    style.configure("Treeview.Heading", background = "#1c1c1c", foreground= "white", borderwidth= 0)

    listbox = ttk.Treeview(root1, selectmode="extended",columns=("c1"), height= 10, show="headings")
    listbox.column("# 1", anchor=CENTER, width = 798)
    listbox.heading("# 1", text="requests")

    for request in requests:
        id1.append(request["student_id"])

    for student in students:
        id2.append(student['_id'])
        first.append(student['first_name'])
        last.append(student['last_name'])

    for i in range(len(id1)):
        for x in range(len(id2)):
            if id1[i] == id2[x]:
                temp = []
                temp.append(first[x])
                temp.append(last[x])
                names.append(temp)
    i = 0
    for request in requests:
        string = names[i][0] + " " + names[i][1] + " is " + request["type"] + " in " + request["name"] + " on " + request["date"]
        listbox.insert(parent= '', index= 'end', iid= i, values= "string")
        i+= 1

    listbox.place(relx= 0.5, rely= 0, anchor= "n")

