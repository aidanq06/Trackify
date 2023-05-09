# Import the required modules
import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import random as rand
from PIL import ImageTk, Image
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://RRHSfbla2023:IheBcYm1ZbOEephx@fbla2023project.wdozi9i.mongodb.net/?retryWrites=true&w=majority")
db = cluster["RRHSfbla2023"]
student_info = db["student_info"]
event_info = db["event_info"]


from about import about
from event import event
#from newStudent import inputStudent
#from report import report
#from winner import pickWinner
#from helper import open_help_window

#connects to the database


conn = sqlite3.connect('studentDatabase.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students (name TEXT, lastname TEXT, grade INTEGER, points INTEGER, number INTEGER)''')
conn.commit()

cursor.execute('SELECT * FROM students')
fetch = cursor.fetchall()

#creates the home GUI
root = tk.Tk()
root.geometry("1000x500")
root.configure(bg='#1c1c1c')
default_font = ctk.CTkFont(size= 18, family= 'Roboto')
large_font = ctk.CTkFont(size= 25, family= 'Roboto')


"""
#creates a label for the home GUI called Student Involment Tracker
left_frame = Frame(root, width = 275, height = 1000, bg= '#242424')
left_frame.place(x = 0, y= 0, anchor = NW)

top_frame = Frame(root, width = 2000, height = 100, bg= '#1c1c1c')
top_frame.place(x = 275, y= 0, anchor = NW)
"""

"""help_image = PhotoImage(file = "./assets/help_image.png")
help2_image = PhotoImage(file = "./assets/help2_image.png")"""
# Open and resize the image
img = Image.open("./assets/logo.png")
img = img.resize((400, 400))
img = ImageTk.PhotoImage(img)

# Create a label to display the image
label = tk.Label(root, image=img)

# Position the label in the center of the window
label.place(relx=0.5, rely=0.5, anchor="center")

"""
# Add a "Edit Student" button to the dialog box
edit_button = ctk.CTkButton(root, text="Edit Student", command=edit_student)
edit_button.place(relx= .225, rely= .8, height= 35, width = 200)"""
"""
# Add a "remove student" button to the dialog box
remove_button = ctk.CTkButton(root, text="Remove student", command= remove_student)
remove_button.place(relx= .425, rely= .8, height= 35, width = 200)"""
"""
# Add a "Edit student points" button to the dialog box
add_points_button = ctk.CTkButton(root, text= "Edit student points", command= add_points)
add_points_button.place(relx= .625, rely= .8, height= 35, width = 200)"""
"""
# Add a "remove all" button to the dialog box
remove_all = ctk.CTkButton(root, text="Remove all", command= remove_everyone)
remove_all.place(relx= .825, rely= .8, height= 35, width = 200)"""

"""
enter = ctk.CTkButton(root, text= "Enter", command= get_entry)
enter.place(relx = .775, rely= .65, height= 25, width= 120, anchor= CENTER)"""
"""
clear = ctk.CTkButton(root, text= "Clear", command= clear)
clear.place(relx = .375, rely= .65, height= 25, width= 120, anchor= CENTER)"""

"""
help_button = tk.Button(root, image= help_image,command=open_help_window, bg="#1c1c1c", fg= "#9b9a92", font= large_font, bd = 0, anchor = "w")
help_button.place(x= 1800, y= 25, anchor=NW)
help_frame = Frame(root, width = 500, height = 900, bg= '#242424')"""
"""
# Allows you to add new students to the database
add_student = tk.Button(root, text="Add new student",command=inputStudent, width=22, bg="#242424", fg= "#9b9a92", font= default_font, bd = 0, anchor = "w")
add_student.place(x= 30, y= 50, anchor=NW)
"""
"""
# Creates a report of the entire database
winner_button = tk.Button(root, text="Pick Winner", command=pickWinner, width=22, bg="#242424", fg= "#9b9a92", font= default_font, bd = 0, anchor= "w")
winner_button.place(x= 30, y= 150, anchor=NW)"""
"""
# Creates a report of the entire database
report_button = tk.Button(root, text="Create Report", command=report, width=22, bg="#242424", fg= "#9b9a92", font= default_font, bd = 0, anchor= "w")
report_button.place(x= 30, y= 250, anchor=NW)
"""

""" 
LEFT SIDE 
"""

# can change the rely to increments of 0.1 to fit more buttons


button = tk.Button(root, text="     Placeholder", command=root.destroy, width=25, bg="#242424", fg= "#9b9a92", font= default_font, bd = 0, anchor= "w")
button.place(relx=0.15,rely=0.4, anchor="center")

button = tk.Button(root, text="     Placeholder", command=root.destroy, width=25, bg="#242424", fg= "#9b9a92", font= default_font, bd = 0, anchor= "w")
button.place(relx=0.15,rely=0.55, anchor="center")

button = tk.Button(root, text="     Placeholder", command=root.destroy, width=25, bg="#242424", fg= "#9b9a92", font= default_font, bd = 0, anchor= "w")
button.place(relx=0.15,rely=0.7, anchor="center")

button = tk.Button(root, text="     Placeholder", command=root.destroy, width=25, bg="#242424", fg= "#9b9a92", font= default_font, bd = 0, anchor= "w")
button.place(relx=0.15,rely=0.85, anchor="center")

"""
RIGHT SIDE

button = tk.Button(root, text="     About Us", command=root.destroy, width=25, bg="#242424", fg= "#9b9a92", font= default_font, bd = 0, anchor= "w")
button.place(relx=0.85,rely=0.1, anchor="center")

button = tk.Button(root, text="     Placeholder", command=root.destroy, width=25, bg="#242424", fg= "#9b9a92", font= default_font, bd = 0, anchor= "w")
button.place(relx=0.85,rely=0.25, anchor="center")

button = tk.Button(root, text="     Placeholder", command=root.destroy, width=25, bg="#242424", fg= "#9b9a92", font= default_font, bd = 0, anchor= "w")
button.place(relx=0.85,rely=0.4, anchor="center")
"""

## IMAGE BUTTONS
event_image = Image.open("./assets/event.png")
event_image = event_image.resize((250, 75))
event_image = ImageTk.PhotoImage(event_image)
event_button = tk.Button(root, image=event_image, command= event)
event_button.place(relx=0.85, rely=0.2, anchor="center")

about_image = Image.open("./assets/about.png")
about_image = about_image.resize((250, 75))
about_image = ImageTk.PhotoImage(about_image)
about_button = tk.Button(root, image=about_image, command=about)
about_button.place(relx=0.85, rely=0.4, anchor="center")

view_image = Image.open("./assets/view_entries.png")
view_image = view_image.resize((250, 75))
view_image = ImageTk.PhotoImage(view_image)
view_button = tk.Button(root, image=view_image, command=about) # CHANGE THIS
view_button.place(relx=0.85, rely=0.6, anchor="center")

help_image = Image.open("./assets/help.png")
help_image = help_image.resize((250, 75))
help_image = ImageTk.PhotoImage(help_image)
help_button = tk.Button(root, image=help_image, command=about) # CHANGE THIS
help_button.place(relx=0.85, rely=0.8, anchor="center")


login_screen = Frame(root, width= 1000, height= 500, bg= '#1c1c1c')
#login_screen.place(relx= 0, rely= 0, anchor= NW)


font = ctk.CTkFont(family= "Quicksand", size= 15, weight= "bold")

sign_in_image = Image.open("./assets/sign_in.png")
sign_in_image = sign_in_image.resize((270, 68))
sign_in_image = ImageTk.PhotoImage(sign_in_image)
sign_in = Label(login_screen, image= sign_in_image, bd= 0)
sign_in.place(relx= .5, rely= .35, anchor= CENTER)

username_entry = ctk.CTkEntry(login_screen, bg_color= "#1C1F1F", border_width= 0, width= 200, font= font, placeholder_text= "username")
username_entry.place(relx= .5, rely= .5, anchor= CENTER)

password_entry = ctk.CTkEntry(login_screen, bg_color= "#1C1F1F", border_width= 0, width= 200, font= font, placeholder_text= "password")
password_entry.place(relx= .5, rely= .65, anchor= CENTER)


def login():
    temp = student_info.find()
    for item in temp:
        try:
            if int(password_entry.get()) == int(item["_id"]) and str(username_entry.get()) == str(item["last_name"]):
                login_screen.place_forget()
                sign_out.place(relx=0.15, rely=0.2, anchor="center")
        except:
            ...
    

login_image = Image.open("./assets/login.png")
login_image = login_image.resize((50, 50))
login_image = ImageTk.PhotoImage(login_image)
login_button = tk.Button(login_screen, image=login_image, command= login) # CHANGE THIS
login_button.place(relx=0.5, rely=0.8, anchor="center")

img1 = Image.open("./assets/logo.png")
img1 = img1.resize((200, 200))
img1 = ImageTk.PhotoImage(img1)


def place_login_frame():
    login_screen.place(relx= 0, rely= 0, anchor= NW)
    sign_out.place_forget()
    username_entry.delete(0, END)
    password_entry.delete(0, END)

sign_out_image = Image.open("./assets/sign_out.png")
sign_out_image = sign_out_image.resize((250, 75))
sign_out_image = ImageTk.PhotoImage(sign_out_image)
sign_out = tk.Button(root, image=sign_out_image, command= place_login_frame)


# keeps gui running
if __name__ == "__main__":
    root.mainloop()
    """
    #closes the cursor
    cursor.close()

    #closes the connection
    conn.close()
    """