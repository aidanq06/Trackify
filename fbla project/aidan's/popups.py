import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from PIL import ImageTk, Image
from tkextrafont import Font

def error(error_message):
    root = tk.Toplevel()
    root.geometry("400x200")
    root.configure(bg='#1c1c1c')
    root.grab_set()

    aboutLabel = ctk.CTkLabel(root, text= error_message,font= ("Quicksand", 20), text_color="white", fg_color= '#1c1c1c', bg_color= '#1c1c1c')
    aboutLabel.place(relx=0.5, rely=0.4, anchor="center")   

    root.mainloop()