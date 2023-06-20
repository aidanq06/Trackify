from subfile import WinnersWindow, ExportNotificationWindow
import tkinter as tk
import random

root = tk.Tk()

def assign_prize(points):
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
            
students = [
    {'name': f'Student {i}', 'points': random.randint(70, 100), 'grade': (i % 4) + 1}
    for i in range(100)
]

winners = {}
for grade in range(1, 5):
    grade_students = [student for student in students if student['grade'] == grade]
    random_winner = random.choice(grade_students)
    top_scorer = max(grade_students, key=lambda student: student['points'])

    random_winner_prize = assign_prize(random_winner['points'])
    top_scorer_prize = assign_prize(top_scorer['points'])

    winners[grade] = {
        'random_winner': (random_winner['name'], random_winner['points'], random_winner_prize),
        'top_scorer': (top_scorer['name'], top_scorer['points'], top_scorer_prize),
    }


winners_window = WinnersWindow(master=root, winners=winners)
winners_window.mainloop()
