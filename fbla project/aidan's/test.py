import sqlite3
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

root = tk.Tk()
root.geometry("500x500")

entry = ctk.CTkEntry(root, width= 200)
entry.insert(0, "hello")

def Entry1_Callback(event):
    entry.select_range(0, END)

entry.bind('<FocusIn>', Entry1_Callback)
entry.pack()

if __name__ == "__main__":
    root.mainloop()




    



