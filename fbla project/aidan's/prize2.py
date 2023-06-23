import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import random
import json
import customtkinter as ctk

import pymongo
from pymongo import MongoClient

from reportlab.pdfgen import canvas
from popups import error

cluster = MongoClient("mongodb+srv://RRHSfbla2023:IheBcYm1ZbOEephx@fbla2023project.wdozi9i.mongodb.net/?retryWrites=true&w=majority")
db = cluster["RRHSfbla2023"]
student_info = db["student_info"]
event_info = db["event_info"]
login_info = db["login_info"]
request_info = db["request_info"]

winners = {}
global export_button

def pick_winners():
    # Fetch all students from the database
    students = list(student_info.find())

    # For each student in the database, create a dictionary with their name, points, grade, and ID
    students = [
        {'name': f'{student["first_name"]} {student["last_name"]}', 'points': student['point'], 'grade': student['grade'], 'id': student['_id']}
        for student in students
    ]

    root = tk.Toplevel()
    root.geometry("+750+50")
    root.title("Prize Winners")
    root.configure(bg='#1c1c1c')

    try:
        for grade in range(9, 13):
            grade_students = [student for student in students if student['grade'] == grade]

            # Pick a random winner
            random_winner = random.choice(grade_students)

            # Remove the random winner from the grade_students list
            grade_students = [student for student in grade_students if student['id'] != random_winner['id']]

            # If there are no other students left in the grade, set the top scorer to "No valid winner"
            if not grade_students:
                top_scorer = {'name': "No valid winner", 'points': 0, 'id': 'N/A'}
            else:
                top_scorer = max(grade_students, key=lambda student: student['points'])

            random_winner_prize = assign_prize(random_winner['points'])
            top_scorer_prize = assign_prize(top_scorer['points'])

            winners[grade] = {
                'random_winner': (random_winner['name'], random_winner['points'], random_winner['id'], random_winner_prize),
                'top_scorer': (top_scorer['name'], top_scorer['points'], top_scorer['id'], top_scorer_prize),
            }
    except:
        ...

    # For each grade, create a frame and place it in the appropriate position in the grid
    grid_positions = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for i, grade in enumerate(range(9, 13), start=0):
        # Set frame background to #1c1c1c and add a white border
        winner_frame = tk.Frame(root, bg='#1c1c1c', highlightthickness=2, highlightbackground='white')
        winner_frame.grid(row=grid_positions[i][0], column=grid_positions[i][1], padx=20, pady=20, sticky='nsew')
        winner_frame.grid_columnconfigure(0, weight=1)


        ctk.CTkLabel(winner_frame, text=f"Grade {grade}", font=("Quicksand", 20), text_color='#1c1c1c', fg_color='white', bg_color="white", corner_radius=5,justify="center").grid(row=0, column=0, sticky='we')

        random_winner_info = winners[grade]['random_winner']
        top_scorer_info = winners[grade]['top_scorer']
        ctk.CTkLabel(winner_frame, text=f"Random winner: {random_winner_info[0]}\nID: {random_winner_info[2]}\nPoints: {random_winner_info[1]}\nPrize: {random_winner_info[3]}\n\nTop scorer: {top_scorer_info[0]}\nID: {top_scorer_info[2]}\nPoints: {top_scorer_info[1]}\nPrize: {top_scorer_info[3]}", font=("Quicksand", 15), padx=10, pady=5, text_color="white", fg_color="#1c1c1c", justify="left").grid(row=1, column=0, sticky="w")

    global export_button
    export_button = ctk.CTkButton(root, height=50, width=300, text='Export Winners', font=("Quicksand", 20), fg_color="white", text_color="#1c1c1c", command=export_winners)
    export_button.grid(row=2, column=0, columnspan=2, pady=10)
    export_button.root = root  # Store root as an attribute of the export_button

    root.mainloop()



def export_winners():

    global winners 
    root = export_button.root
    c = canvas.Canvas('winners.pdf')

    for i, grade in enumerate(range(9, 13), start=1):
        c.drawString(100, 800 - 100 * i, f"Grade {grade}:")

        random_winner_info = winners[grade]['random_winner']
        c.drawString(100, 800 - 100 * i - 15, f"Random winner: {random_winner_info[0]}, ID: {random_winner_info[2]}, Points: {random_winner_info[1]}, Prize: {random_winner_info[3]}")

        top_scorer_info = winners[grade]['top_scorer']
        c.drawString(100, 800 - 100 * i - 30, f"Top scorer: {top_scorer_info[0]}, ID: {top_scorer_info[2]}, Points: {top_scorer_info[1]}, Prize: {top_scorer_info[3]}")

    c.save()

    # create a new window after successfully exported the PDF
    new_window = tk.Toplevel()
    new_window.geometry("+750+500")
    new_window.title("PDF Export Successful")
    new_window.configure(bg='#1c1c1c')

    label = tk.Label(new_window, text="PDF Export Successful!", font=("Quicksand", 25), bg='#1c1c1c', fg='white',padx=20,pady=20)
    label.pack(pady=10)

    # Define a function to close both windows
    def close_both_windows():
        new_window.destroy()
        root.destroy()

    # Call close_both_windows when the new_window's close button is clicked
    new_window.protocol("WM_DELETE_WINDOW", close_both_windows)

    new_window.mainloop()



def assign_prize(points):
    # Prizes: each tuple represents (points threshold, prize)
    prizes = [
        (0, "N/A"),
        (1, "Free snack from school store"),
        (75, 'Free homework pass'),
        (100, 'Free lunch and free snack'),
        (125, 'Free entry to next school-related event'),
        (150, 'Choice of any school-spirited apparel (hoodie, shirt, etc.)'),
    ]
    # Assign the highest prize the student's points qualify for
    for threshold, prize in reversed(prizes):
        if points >= threshold:
            return prize

