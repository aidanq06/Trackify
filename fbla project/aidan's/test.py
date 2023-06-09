from tkinter import *
import tkinter as tk
from tkinter import ttk

def idk():
    root = tk.Tk()
    root.geometry("1000x500")
    root.configure(bg= '#1c1c1c')

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", fieldbackground= "#1c1c1c", background = "#242424", foreground= "#9b9a92")
    
    listbox = ttk.Treeview(root, selectmode="extended",columns=("c1", "c2", "c3", "c4", "c5"),show="headings", height= 12)
    listbox.column("# 1", anchor=CENTER, width = 199)
    listbox.heading("# 1", text="Student id")
    listbox.column("# 2", anchor=CENTER, width = 199)
    listbox.heading("# 2", text="First Name")
    listbox.column("# 3", anchor=CENTER, width = 199)
    listbox.heading("# 3", text="Last Name")
    listbox.column("# 4", anchor=CENTER, width = 199)
    listbox.heading("# 4", text="Grade Level")
    listbox.column("# 5", anchor=CENTER, width = 199)
    listbox.heading("# 5", text="Points")

    listbox.place(relx= 0, rely= 0, anchor= "nw")
    
    if __name__ == "__main__":
        root.mainloop()

idk()

