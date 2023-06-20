import tkinter as tk
import customtkinter as ctk

from PIL import ImageTk, Image


def about():
    root1 = tk.Toplevel()
    root1.geometry("600x600")
    root1.configure(bg='#1c1c1c')

    def close():
        root1.destroy()

    aboutLabel = ctk.CTkLabel(root1,text="About Us", font=("Quicksand",32), text_color="white")
    aboutLabel.place(relx=0.50, rely=0.2, anchor="center")

    aboutText = ctk.CTkLabel(root1,text="Hello", font=("Quicksand",16), text_color="white")
    aboutText.place(relx=0.50, rely=0.4, anchor="center")

    back_image = Image.open("./assets/back.png")
    back_image = back_image.resize((50, 40))
    back_image = ImageTk.PhotoImage(back_image)   
    back_button = tk.Button(root1, image=back_image, border = 0, highlightthickness = 0, command= close)
    back_button.image = back_image
    back_button.place(relx=0.075, rely=0.075, anchor="center")

    root1.mainloop()
   