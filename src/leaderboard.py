import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://RRHSfbla2023:IheBcYm1ZbOEephx@fbla2023project.wdozi9i.mongodb.net/?retryWrites=true&w=majority")
db = cluster["RRHSfbla2023"]
student_info = db["student_info"]
event_info = db["event_info"]
login_info = db["login_info"]
request_info = db["request_info"]

def leaderboard(grade):
    # Fetch all students from the same grade from the database
    students = list(student_info.find({"grade": grade}))

    # Sort the students based on their points in descending order
    students.sort(key=lambda x: x['point'], reverse=True)

    root = tk.Toplevel()
    root.geometry("400x700")
    root.resizable(False, False)
    root.title(f"Leaderboard")
    root.configure(bg="#1c1c1c")

    # Set the Quicksand font for the Treeview
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", fieldbackground="#1c1c1c", background="#1c1c1c", foreground="white", font=("Quicksand", 12),
                    rowheight=80, highlightbackground="#1c1c1c", highlightcolor="#1c1c1c", borderwidth=1)
    style.configure("Treeview.Heading", background="#1c1c1c", foreground="white", borderwidth=0, font=("Quicksand", 12))

    # Create a title label for the leaderboard
    title_label = tk.Label(root, text=f"Leaderboard\nGrade: {grade}", font=("Quicksand", 20), bg="#1c1c1c", fg="white")
    title_label.pack(pady=10)

    # Create a Treeview widget to display the leaderboard
    leaderboard_tree = ttk.Treeview(root, selectmode="none", columns=("Name", "Points"), show="headings")
    leaderboard_tree.column("Name", anchor=tk.CENTER, width=225)
    leaderboard_tree.heading("Name", text="Name")
    leaderboard_tree.column("Points", anchor=tk.CENTER, width=75)
    leaderboard_tree.heading("Points", text="Points")
    leaderboard_tree.pack(fill="both", expand=True)  # Allow the Treeview to expand vertically

    # Set the row height of the Treeview
    row_height = 28  # Adjust the row height as per your preference
    leaderboard_tree.configure(height=row_height)

    # Insert student data into the leaderboard Treeview
    for index, student in enumerate(students, start=1):
        leaderboard_tree.insert("", "end", values=(f"{student['first_name']} {student['last_name']} - #{index} ", student["point"]))

    root.mainloop()
