from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import customtkinter 

app = customtkinter.CTk()
optionmenu_var = customtkinter.StringVar(value="option 2")  # set initial value

def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

combobox = customtkinter.CTkComboBox(master=app,
                                     values=["1", "2"],
                                     variable=optionmenu_var)
combobox.pack(padx=20, pady=10)
if __name__ == "__main__":
    app.mainloop()

