import customtkinter as ctk
from tkinter import *

from main import connect_to_db

cursor = connect_to_db()

# Error Window (input an error message argument to display)
def error(self, error=str):

    def close():
        eWin.destroy()

    eWin = ctk.CTkToplevel()
    eWin.title("Error!")
    eWin.geometry("400x100")

    Label = ctk.CTkLabel(eWin, text=error,corner_radius=10)
    Label.place(relx=0.5,rely=.3, anchor=CENTER)
    
    close_button = ctk.CTkButton(eWin, text="Close", command=close)
    close_button.place(relx=0.5,rely=0.7, anchor=CENTER)

# Success Window (input a success message argument to display)
def success(self, success=str):

    def close():
        sWin.destroy()

    sWin = ctk.CTkToplevel()
    sWin.title("Success!")
    sWin.geometry("400x100")

    Label = ctk.CTkLabel(sWin, text=success,corner_radius=10)
    Label.place(relx=0.5,rely=.3, anchor=CENTER)
    
    close_button = ctk.CTkButton(sWin, text="Close", command=close)
    close_button.place(relx=0.5,rely=0.7, anchor=CENTER)

    # Define a function to be called when the "edit student" button is clicked