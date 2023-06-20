import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import random
import json
import customtkinter as ctk
from reportlab.pdfgen import canvas

class WinnersWindow(tk.Toplevel):
    def __init__(self, master=None, winners=None, **kwargs):
        super().__init__(master, **kwargs)

        self.winners = winners
        self.notification_window = None  # initially, there's no notification window

        self.configure(bg='black')  # set window background to black
        self.title('Prize Winners')

        for i, grade in enumerate(range(1, 5), start=1):
            winner_frame = tk.Frame(self, bg='black')  # set frame background to black
            winner_frame.grid(row=i, column=0, pady=10)

            ttk.Label(winner_frame, text=f"Grade {grade}:", font=("Arial", 14), foreground='white', background='black').grid(row=0, column=0)  # set text color to white, background to black

            random_winner_info = winners[grade]['random_winner']
            ttk.Label(winner_frame, text=f"Random winner: {random_winner_info[0]}, Points: {random_winner_info[1]}, Prize: {random_winner_info[2]}", font=("Arial", 12), foreground='white', background='black').grid(row=1, column=0)

            top_scorer_info = winners[grade]['top_scorer']
            ttk.Label(winner_frame, text=f"Top scorer: {top_scorer_info[0]}, Points: {top_scorer_info[1]}, Prize: {top_scorer_info[2]}", font=("Arial", 12), foreground='white', background='black').grid(row=2, column=0)

        self.export_button = ctk.CTkButton(self, text='Export Winners', command=self.export_winners)
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
        
        self.notification_window = ExportNotificationWindow(self)

class ExportNotificationWindow(tk.Toplevel):
    def __init__(self, master=None, winners_window=None, **kwargs):
        super().__init__(master, **kwargs)

        self.winners_window = winners_window  # keep reference to the winners window

        self.configure(bg='black')  # set window background to black
        self.title('Export Notification')

        ctk.CTkLabel(self, text='Winners exported to winners.pdf', font=("Arial", 14), fg='white', bg='black').pack(pady=20)
        
        self.protocol("WM_DELETE_WINDOW", self.on_close)  # bind closing event to custom on_close method

    def on_close(self):
        self.winners_window.destroy()  # destroy winners window
        self.destroy()  # destroy this window
