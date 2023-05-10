import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
import pyglet
from PIL import ImageTk, Image

pyglet.font.add_file("./assets/Quicksand_Bold.otf")


def error(error_message):
    root = tk.Toplevel()
    root.geometry("400x200")
    root.configure(bg='#1c1c1c')

    def close():
        root.destroy()

    aboutLabel = ctk.CTkLabel(root, text= error_message,font= ("Quicksand_bold", 20, "bold"), text_color="white")
    aboutLabel.place(relx=0.5, rely=0.3333, anchor="center")

    back_image = Image.open("./assets/back.png")
    back_image = back_image.resize((50, 40))
    back_image = ImageTk.PhotoImage(back_image)   
    back_button = tk.Button(root, image=back_image, border = 0, highlightthickness = 0, command= close)
    back_button.image = back_image
    back_button.place(relx=0.5, rely=0.6666, anchor="center")

    

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