import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import random

class StudentPrizeApp(tk.Tk):
    def __init__(self, student_data):
        super().__init__()

        self.student_data = student_data

        self.title("Student Prize App")
        self.geometry('300x200')

        self.report_button = tk.Button(self, text='Generate Report', command=self.generate_report)
        self.report_button.pack(pady=20)

        self.prize_button = tk.Button(self, text='Pick Prize Winners', command=self.pick_winners)
        self.prize_button.pack(pady=20)

    def generate_report(self):
        with PdfPages('student_report.pdf') as pdf:
            for grade in range(1, 5):
                self.create_report(pdf, grade=grade)
            self.create_report(pdf)

        messagebox.showinfo("Report generated", "The student report was successfully generated.")

    def create_report(self, pdf, grade=None):
        # Similar code to the create_report function shared earlier
        ...

    def pick_winners(self):
        winners = {}
        for grade in range(1, 5):
            grade_students = [student for student in self.student_data if student['grade'] == grade]
            random_winner = random.choice(grade_students)
            top_scorer = max(grade_students, key=lambda student: student['points'])

            random_winner_prize = self.assign_prize(random_winner['points'])
            top_scorer_prize = self.assign_prize(top_scorer['points'])

            winners[grade] = {
                'random_winner': (random_winner['name'], random_winner_prize),
                'top_scorer': (top_scorer['name'], top_scorer_prize),
            }

        message = "\n".join(
            f"Grade {grade}:\n"
            f"  Random winner: {winners[grade]['random_winner'][0]} ({winners[grade]['random_winner'][1]})\n"
            f"  Top scorer: {winners[grade]['top_scorer'][0]} ({winners[grade]['top_scorer'][1]})"
            for grade in range(1, 5)
        )
        messagebox.showinfo("Prize winners", message)

    def assign_prize(self, points):
            # Prizes: each tuple represents (points threshold, prize)
        prizes = [
            (80, 'school reward'),
            (85, 'food reward'),
            (90, 'school spirit item'),
        ]
        # Assign the highest prize the student's points qualify for
        for threshold, prize in reversed(prizes):
            if points >= threshold:
                return prize
        # If the student's points do not qualify for any prize, return a consolation message
        return 'Better luck next time!'

# example student data
students = [
    {'name': f'Student {i}', 'points': random.randint(70, 100), 'grade': (i % 4) + 1}
    for i in range(100)
]

app = StudentPrizeApp(students)
app.mainloop()
