import tkinter as tk
import customtkinter as ctk

from PIL import ImageTk, Image


def about():
    root1 = tk.Toplevel()
    root1.geometry("600x600")
    root1.configure(bg='#1c1c1c')

    def close():
        root1.destroy()

    aboutText = Image.open("./assets/logo.png")
    aboutText = aboutText.resize((400, 400))
    aboutText = ImageTk.PhotoImage(aboutText)
    aboutLabel = tk.Label(root1,image=aboutText, border= 0)
    aboutLabel.image = aboutText
    aboutLabel.place(relx=0.5, rely=0.5, anchor="center")

    back_image = Image.open("./assets/back.png")
    back_image = back_image.resize((30, 23))
    back_image = ImageTk.PhotoImage(back_image)   
    back_button = tk.Button(root1, image=back_image, border = 0, highlightthickness = 0, command= close)
    back_button.image = back_image
    back_button.place(relx=0.1, rely=0.1, anchor="center")

    root1.mainloop()
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
   