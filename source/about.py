import tkinter as tk
import customtkinter as ctk

from PIL import ImageTk, Image


def about():
    root1 = tk.Toplevel()
    root1.geometry("600x600")
    root1.configure(bg='#1c1c1c')
    root1.grab_set()
    root1.resizable(False,False)
    
    text = """Welcome to our Future Business Leaders of America (FBLA) Programming and Coding project for 2022-2023! We, Aidan Quach and Harishankar Rajesh, are sophomores at River Ridge High School and have spent the last seven months developing a student-involvement tracker. Our system is designed to motivate student engagement by awarding points for involvement in school activities, which can be redeemed for rewards.
    \n\nThis project involved in-depth learning of various software development facets, while also enhancing our ability to devise effective solutions to complex problems. The journey was challenging but rewarding, with the final product serving as both a tool for fostering a more interactive educational environment and a testament to our journey into the world of programming."""

    def close():
        root1.destroy()

    aboutLabel = ctk.CTkLabel(root1,text="About Us", font=("Quicksand",32), text_color="white")
    aboutLabel.place(relx=0.50, rely=0.1, anchor="center")

    aboutText = ctk.CTkLabel(root1,text=text, font=("Quicksand",16), text_color="white", wraplength=550)
    aboutText.place(relx=0.50, rely=0.5, anchor="center")

    back_image = Image.open("back.png")
    back_image = back_image.resize((50, 40))
    back_image = ImageTk.PhotoImage(back_image)   
    back_button = tk.Button(root1, image=back_image, border = 0, highlightthickness = 0, command= close)
    back_button.image = back_image
    back_button.place(relx=0.075, rely=0.075, anchor="center")

    root1.mainloop()
