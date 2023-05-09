import tkinter as tk
import customtkinter as ctk
from tkinter import ttk

from PIL import ImageTk, Image


def error():
    root = tk.Toplevel()
    root.geometry("600x600")
    root.configure(bg='#1c1c1c')

    font = ctk.CTkFont(family= "Quicksand", size= 50, weight= "bold")

    def close():
        root.destroy()

    """aboutText = Image.open("./assets/aboutText.png")
    aboutText = aboutText.resize((500, 500))
    aboutText = ImageTk.PhotoImage(aboutText)"""
    #aboutLabel = tk.Label(root1,image=aboutText, border= 0)
    #aboutLabel.image = aboutText

    aboutLabel = ctk.CTkLabel(root,text="hello",font=font,text_color="white")
    aboutLabel.place(relx=0.5, rely=0.5, anchor="center")

    back_image = Image.open("./assets/back.png")
    back_image = back_image.resize((50, 40))
    back_image = ImageTk.PhotoImage(back_image)   
    back_button = tk.Button(root, image=back_image, border = 0, highlightthickness = 0, command= close)
    back_button.image = back_image
    back_button.place(relx=0.075, rely=0.075, anchor="center")

    root.mainloop()
    """
    aWin = ctk.CTkToplevel()
    aWin.title("About us")
    aWin.geometry("400x100")
    """
    """
    Label = ctk.CTkLabel(aWin, text="HELLO",corner_radius=10)
    Label.place(relx=0.5,rely=.3, anchor="center")
    """
    """
    close_button = ctk.CTkButton(aWin, text="Close", command=close)
    close_button.place(relx=0.5,rely=0.7, anchor="center")
    """
   
"""
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
"""