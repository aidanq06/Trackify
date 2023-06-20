import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import random
import json
import customtkinter as ctk

from tkextrafont import Font
from reportlab.pdfgen import canvas


class WinnersWindow(tk.Toplevel):
    def __init__(self, winners):
        super().__init__()
        
        self.winners = winners
        self.title("Student Prize App")
        self.geometry('600x400')
        self.geometry("+50+50")
        self.font = Font(file="./assets/Quicksand-Bold.ttf", family="Quicksand")
        self.configure(bg='#1C1F1F')  # set window background to #1C1F1F
        self.title('Prize Winners')
        self.geometry("+750+50")

        for i, grade in enumerate(range(1, 5), start=1):
            winner_frame = tk.Frame(self, bg='#1C1F1F')  # set frame background to #1C1F1F
            winner_frame.grid(row=i, column=0, pady=10)

            ctk.CTkLabel(winner_frame, text=f"Grade {grade}:", font=("Quicksand", 18), text_color='#1C1F1F', fg_color='white', corner_radius=5).grid(row=0, column=0)  # set text color to white, background to #1C1F1F

            random_winner_info = winners[grade]['random_winner']
            top_scorer_info = winners[grade]['top_scorer']
            ctk.CTkLabel(winner_frame, text=f"Random winner: {random_winner_info[0]}\nPoints: {random_winner_info[1]}\nPrize: {random_winner_info[2]}\n\nTop scorer: {top_scorer_info[0]}\nPoints: {top_scorer_info[1]}\nPrize: {top_scorer_info[2]}", font=("Quicksand", 15), padx=50,pady=5,text_color="white",fg_color="#1C1F1F",justify="left").grid(row=1, column=0)

            
        self.export_button = ctk.CTkButton(self, height=50, width=300, text='Export Winners', font=("Quicksand",20), fg_color="white", text_color="#1C1F1F", command=self.export_winners)
        self.export_button.grid(row=5, column=0, pady=10)
    
    def export_winners(self):
        c = canvas.Canvas('winners.pdf')

        for i, grade in enumerate(range(1, 5), start=1):
            c.drawString(100, 800 - 100 * i, f"Grade {grade}:")

            random_winner_info = self.winners[grade]['random_winner']
            c.drawString(100, 800 - 100 * i - 15, f"Random winner: {random_winner_info[0]}, Points: {random_winner_info[1]}, Prize: {random_winner_info[2]}")

            top_scorer_info = self.winners[grade]['top_scorer']
            c.drawString(100, 800 - 100 * i - 30, f"Top scorer: {top_scorer_info[0]}, Points: {top_scorer_info[1]}, Prize: {top_scorer_info[2]}")

        c.save()

        ExportNotificationWindow(self)


class ExportNotificationWindow(tk.Toplevel):
    def __init__(self,winners_window):
        super().__init__()
        self.winners_window = winners_window 
        self.configure(bg='#1C1F1F')
        self.title('Export Notification')
        self.geometry("+750+500")

        ctk.CTkLabel(self, text='Winners and prize data has been exported to winners.pdf', font=("Quicksand", 35), fg_color='#1C1F1F', bg_color="#1C1F1F",text_color='white').pack(pady=20,padx=20)
        self.protocol("WM_DELETE_WINDOW", self.on_close)  # bind closing event to custom on_close method

    def on_close(self):
        self.winners_window.destroy()  # destroy winners window
        self.destroy()  # destroy this window
        
class StudentPrizeApp(tk.Toplevel):
    root = tk.Toplevel()
    
    def __init__(self):
        super().__init__()

    def pick_winners(self):
        students = [
            {'name': f'Student {i}', 'points': random.randint(70, 100), 'grade': (i % 4) + 1}
            for i in range(100)
        ]

        winners = {}
        for grade in range(1, 5):
            grade_students = [student for student in self.students if student['grade'] == grade]
            random_winner = random.choice(grade_students)
            top_scorer = max(grade_students, key=lambda student: student['points'])

            random_winner_prize = self.assign_prize(random_winner['points'])
            top_scorer_prize = self.assign_prize(top_scorer['points'])

            winners[grade] = {
                'random_winner': (random_winner['name'], random_winner['points'], random_winner_prize),
                'top_scorer': (top_scorer['name'], top_scorer['points'], top_scorer_prize),
            }
            

        WinnersWindow(winners)
        

    def assign_prize(self, points):
        # Prizes: each tuple represents (points threshold, prize)
        prizes = [
            (0, "Free snack from school store"),
            (93, 'Free homework pass'),
            (95, 'Free entry to next school-related event'),
            (97, 'Choice of any school-spirited apparel (hoodie, shirt, etc.)'),
        ]
        # Assign the highest prize the student's points qualify for
        for threshold, prize in reversed(prizes):
            if points >= threshold:
                return prize

# example student data
