# Import the required modules
import sqlite3
from tkinter import *
import tkinter as tk
import customtkinter as ctk
import random as rand

from PIL import ImageTk, Image

#from newStudent import inputStudent
#from report import report
#from winner import pickWinner
#from helper import open_help_window

#connects to the database

def connect_to_db():
    conn = sqlite3.connect('studentDatabase.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (name TEXT, lastname TEXT, grade INTEGER, points INTEGER, number INTEGER)''')
    conn.commit()
    return cursor

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
img = img.resize((400, 400), Image.ANTIALIAS)
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
button = tk.Button(root, text="     Quit", command=root.destroy, width=25, bg="#242424", fg= "#9b9a92", font= default_font, bd = 0, anchor= "w")
button.place(relx=0.15,rely=0.1, anchor="center")

button = tk.Button(root, text="     Placeholder", command=root.destroy, width=25, bg="#242424", fg= "#9b9a92", font= default_font, bd = 0, anchor= "w")
button.place(relx=0.15,rely=0.25, anchor="center")

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
event_image = Image.open("./assets/events.png")
event_image = event_image.resize((250, 75), Image.ANTIALIAS)
event_image = ImageTk.PhotoImage(event_image)
button = tk.Button(root, image=event_image)
button.place(relx=0.85, rely=0.2, anchor="center")

about_image = Image.open("./assets/about.png")
about_image = about_image.resize((250, 75), Image.ANTIALIAS)
tk_image2 = ImageTk.PhotoImage(about_image)
button = tk.Button(root, image=tk_image2)
button.place(relx=0.85, rely=0.4, anchor="center")



# keeps gui running
if __name__ == "__main__":
    root.mainloop()
    """
    #closes the cursor
    cursor.close()

    #closes the connection
    conn.close()
    """