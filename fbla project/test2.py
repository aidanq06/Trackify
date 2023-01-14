from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ctk

window = tk.Tk()
my_entry = ctk.CTkEntry(window)
my_entry.insert(tk.END, "default text")
my_entry.pack()
my_entry.bind("<Button-1>", lambda a: my_entry.delete(0, tk.END))
if __name__ == "__main__":
    window.mainloop()

