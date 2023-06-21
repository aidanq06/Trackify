from tkinter import *
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import random as rand
from PIL import ImageTk, Image
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://RRHSfbla2023:IheBcYm1ZbOEephx@fbla2023project.wdozi9i.mongodb.net/?retryWrites=true&w=majority")
db = cluster["RRHSfbla2023"]
student_info = db["student_info"]
event_info = db["event_info"]
login_info = db["login_info"]
request_info = db["request_info"]


def view_requests():

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", fieldbackground= "#1c1c1c", background = "#1c1c1c", foreground= "white", font= ("Quicksand", 12), rowheight= 80, highlightbackground = "#1c1c1c", highlightcolor= "#1c1c1c", borderwidth= 1)
    style.configure("Treeview.Heading", background = "#1c1c1c", foreground= "white", borderwidth= 0, font= ("Quicksand", 12))
    
    root1 = tk.Toplevel()
    root1.geometry("1200x600")
    root1.configure(bg= '#1c1c1c')
    temp = list()
    points = list()
    final = list()
    dates = list()

    listbox = ttk.Treeview(root1, selectmode="extended",columns=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"), height= 6, show="headings")
    listbox.column("# 1", anchor=CENTER, width = 149)
    listbox.heading("# 1", text="id")

    listbox.column("# 2", anchor=CENTER, width = 149)
    listbox.heading("# 2", text="first name")

    listbox.column("# 3", anchor=CENTER, width = 149)
    listbox.heading("# 3", text="last name")

    listbox.column("# 4", anchor=CENTER, width = 149)
    listbox.heading("# 4", text="grade")

    listbox.column("# 5", anchor=CENTER, width = 149)
    listbox.heading("# 5", text="event")

    listbox.column("# 6", anchor=CENTER, width = 149)
    listbox.heading("# 6", text="date")

    listbox.column("# 7", anchor=CENTER, width = 149)
    listbox.heading("# 7", text="involvement")

    listbox.column("# 8", anchor=CENTER, width = 149)
    listbox.heading("# 8", text="points")

    requests = request_info.find()
    for request in requests:
        temp = []
        temp.append(request["date"].split("-"))
        dates.append(f'{temp[0][1]}/{temp[0][2]}/{temp[0][0]}')

    requests = request_info.find()
    for i in range(len(dates)):
        events = event_info.find()
        for event in events:
            if dates[i] == event['date'] and requests[i]['name'] == event['name']:
                points.append(event['points'])

    requests = request_info.find()
    for request in requests:
        students = student_info.find()
        for student in students:
            if request["student_id"] == student["_id"]:
                temp = []
                temp.append(student)
                temp.append(request)
                final.append(temp)

    count = 0
    for item in final:
        if item[1]["status"] == "pending":
            listbox.insert(parent='', index='end', text= "", iid= count, values= (item[0]["_id"], item[0]["first_name"], item[0]["last_name"], item[0]["grade"], item[1]["name"], item[1]["date"], item[1]["type"], points[count]))
            count += 1

    def refresh():
        for item in listbox.get_children():
            listbox.delete(item)

        count1 = 0
        for item in final:
            print(item)
            if item[1]["status"] == "pending":
                listbox.insert(parent='', index='end', text= "", iid= count1, values= (item[0]["_id"], item[0]["first_name"], item[0]["last_name"], item[0]["grade"], item[1]["name"], item[1]["date"], item[1]["type"], points[count1]))
                count1+= 1
        listbox.place(relx= 0, rely= 0, anchor= "nw")

    def approve():
        items = listbox.selection()
        
        if len(items) > 0:
            for item in items:
                selection = listbox.item(item, option="values")
                students = student_info.find()
                for student in students:
                    if int(student["_id"]) == int(selection[0]):
                        point = student["point"]
                point = int(point) + int(selection[7])
                student_info.update_one({"_id": int(selection[0])}, {"$set":{"points": int(point)}})
                request_info.update_one({"student_id": int(selection[0]), "name": str(selection[4]), "date": str(selection[5])}, {"$set":{"status": "approved"}})
            
                refresh()





    listbox.place(relx= 0.5, rely= 0, anchor= "n")

    approve = ctk.CTkButton(root1, text= "approve", font= ("Quicksand", 25), command= approve, bg_color= "#1c1c1c", fg_color= "#1c1c1c", text_color= "white", hover_color="#1c1c1c")
    approve.place(relx= 0.2, rely= 0.925, anchor="center")
        



