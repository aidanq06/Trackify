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
    root.geometry("300x692")
    root.resizable(False, False)
    root.title("Leaderboard")
    root.configure(bg="#1c1c1c")

    # Set the Quicksand font for the Treeview
    style = ttk.Style()
    style.configure("Treeview", font=("Quicksand", 12), background="#1c1c1c", foreground="white", highlightthickness=0)
    style.configure("Treeview.Heading", font=("Quicksand", 12, "bold"), background="#1c1c1c", foreground="#1c1c1c")

    # Create a title label for the leaderboard
    title_label = tk.Label(root, text="Leaderboard", font=("Quicksand", 20), bg="#1c1c1c", fg="white")
    title_label.pack(pady=10)

    # Create a Treeview widget to display the leaderboard
    leaderboard_tree = ttk.Treeview(root, selectmode="none", columns=("Name", "Points"), show="headings")
    leaderboard_tree.column("Name", width=225)
    leaderboard_tree.heading("Name", text="Name")
    leaderboard_tree.column("Points", width=75)
    leaderboard_tree.heading("Points", text="Points")
    leaderboard_tree.pack(fill="both", expand=True)  # Allow the Treeview to expand vertically

    # Increase the vertical spacing between Treeview entries
    style.configure("Treeview.Item", padding=(0, 4))  # Adjust the padding as per your preference

    # Set the row height of the Treeview
    row_height = 28  # Adjust the row height as per your preference
    leaderboard_tree.configure(height=row_height)

    # Insert student data into the leaderboard Treeview
    for index, student in enumerate(students, start=1):
        leaderboard_tree.insert("", "end", values=(student["first_name"] + " " + student["last_name"], student["point"]))

    root.mainloop()
