from tkinter import *
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry("1000x500")
root.configure(bg= '#1c1c1c')
button1 = tk.Button(root, text= "press me", command= root.deiconify)
button1.pack()
root.withdraw()


if __name__ == "__main__":
    root.mainloop()

    



