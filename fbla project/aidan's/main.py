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
import datetime
import random
from tkextrafont import Font

cluster = MongoClient("mongodb+srv://RRHSfbla2023:IheBcYm1ZbOEephx@fbla2023project.wdozi9i.mongodb.net/?retryWrites=true&w=majority")
db = cluster["RRHSfbla2023"]
student_info = db["student_info"]
event_info = db["event_info"]
login_info = db["login_info"]
request_info = db["request_info"]

from about import about
from event import event
from register import register
from popups import error
from add_student import add_student
from view_requests import view_requests
from create_report2 import createReport
#from prizes import WinnersWindow, ExportNotificationWindow, StudentPrizeApp
from prize2 import pick_winners

#from newStudent import inputStudent
#from report import report
#from winner import pickWinner
#from helper import open_help_window

student_id = 0
#creates the home GUI
root = tk.Tk()
root.geometry("1000x500")
root.configure(bg='#1c1c1c')
font = Font(file="./assets/Quicksand-Bold.ttf", family="Quicksand")

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", fieldbackground= "#1c1c1c", background = "#1c1c1c", foreground= "white", font= ("none", 10), rowheight= 80, highlightbackground = "#1c1c1c", highlightcolor= "#1c1c1c")
style.configure("Treeview.Heading", background = "#1c1c1c", foreground= "white", borderwidth= 0)

root1 = tk.Toplevel()
root1.geometry("1000x500")
root1.configure(bg= '#1c1c1c')
students = student_info.find()

listbox = ttk.Treeview(root1, selectmode="extended",columns=("c1", "c2", "c3", "c4", "c5"),show="headings", height= 10)
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



def refresh():
    for item in listbox.get_children():
        listbox.delete(item)
    students= student_info.find()
    count = 0
    for student in students:
        listbox.insert(parent='', index='end', text= "", iid= count, values= (student["_id"], student["first_name"], student["last_name"], student["grade"], student["point"]) )
        count+= 1
    listbox.place(relx= 0, rely= 0, anchor= "nw")

refresh()

def remove_student():
    item = listbox.selection()
    selection = listbox.item(item, option="values")
    temp = student_info.find()
    for student in temp:
        if int(student["_id"]) == int(selection[0]):
            print(student_info.delete_one({"_id": student["_id"]}))
    refresh()

def edit_student():
    item = listbox.selection()
    selection = listbox.item(item, option="values")

    edit_student_window = tk.Toplevel()
    edit_student_window.geometry("400x600")
    edit_student_window.configure(bg= '#1c1c1c')

    first_entry = ctk.CTkEntry(edit_student_window, bg_color= "#1C1C1C", border_width= 0, width= 200, font= ("Quicksand_bold", 15, "bold"))
    first_entry.insert(0, selection[1])
    def first_select(event):
        first_entry.select_range(0, END)
    first_entry.bind("<FocusIn>", first_select)
    first_entry.place(relx= 0.5, rely= 0.2, anchor= "center")

    last_entry = ctk.CTkEntry(edit_student_window, bg_color= "#1C1F1F", border_width= 0, width= 200, font= ("Quicksand_bold", 15, "bold"))
    last_entry.insert(0, selection[2])
    def last_select(event):
        last_entry.select_range(0, END)
    last_entry.bind("<FocusIn>", last_select)
    last_entry.place(relx= 0.5, rely= 0.4, anchor= "center")

    grade_entry = ctk.CTkEntry(edit_student_window, bg_color= "#1C1F1F", border_width= 0, width= 200, font= ("Quicksand_bold", 15, "bold"))
    grade_entry.insert(0, selection[3])
    def grade_select(event):
        grade_entry.select_range(0, END)
    grade_entry.bind("<FocusIn>", grade_select)
    grade_entry.place(relx= 0.5, rely= 0.6, anchor= "center")

    def get_submit():

        first= first_entry.get()
        last= last_entry.get()
        grade= grade_entry.get()
        student_info.update_one({"_id": int(selection[0])}, {"$set":{"first_name": str(first).capitalize(), "last_name": (str(last).capitalize()), "grade": int(grade)}})

        refresh()
        edit_student_window.destroy()

    submit_button = tk.Button(edit_student_window, text= "submit", command= get_submit)
    submit_button.place(relx= 0.5, rely= 0.8, anchor= "center")


root1.withdraw()

# Open and resize the image
img = Image.open("./assets/logo.png")
img = img.resize((400, 400))
img = ImageTk.PhotoImage(img)
label = tk.Label(root, image=img)

## IMAGE BUTTONS

edit_student_image = Image.open("./assets/edit_student.png")
edit_student_image = edit_student_image.resize((150, 45))
edit_student_image = ImageTk.PhotoImage(edit_student_image)
edit_button = tk.Button(root1, command= edit_student, image= edit_student_image, borderwidth= 0)
edit_button.place(relx= 0.15, rely= 0.875, anchor= "nw")

remove_student_image = Image.open("./assets/remove_student.png")
remove_student_image = remove_student_image.resize((150, 45))
remove_student_image = ImageTk.PhotoImage(remove_student_image)
remove_button = tk.Button(root1, command= remove_student, image= remove_student_image, borderwidth= 0)
remove_button.place(relx= 0.5, rely= 0.875, anchor= "n")

save_exit_image = Image.open("./assets/save_exit.png")
save_exit_image = save_exit_image.resize((150, 45))
save_exit_image = ImageTk.PhotoImage(save_exit_image)
quit_button = tk.Button(root1, command= root1.withdraw, borderwidth= 0, image= save_exit_image)
quit_button.place(relx= 0.85, rely= 0.875, anchor= "ne")

event_image = Image.open("./assets/event.png")
event_image = event_image.resize((250, 75))
event_image = ImageTk.PhotoImage(event_image)
event_button = tk.Button(root, image=event_image, command=event)

add_student_image = Image.open("./assets/add_student.png")
add_student_image = add_student_image.resize((250, 75))
add_student_image = ImageTk.PhotoImage(add_student_image)
add_student_button = tk.Button(root, image=add_student_image, command=add_student)

about_image = Image.open("./assets/about.png")
about_image = about_image.resize((250, 75))
about_image = ImageTk.PhotoImage(about_image)
about_button = tk.Button(root, image=about_image, command=about)

view_image = Image.open("./assets/view_entries.png")
view_image = view_image.resize((250, 75))
view_image = ImageTk.PhotoImage(view_image)
view_button = tk.Button(root, image=view_image, command= root1.deiconify) # CHANGE THIS

create_report_image = Image.open("./assets/create_report.png")
create_report_image = create_report_image.resize((250, 75))
create_report_image = ImageTk.PhotoImage(create_report_image)
create_report_button = tk.Button(root, command= createReport, image= create_report_image)

view_requests_image = Image.open("./assets/view_requests.png")
view_requests_image = view_requests_image.resize((250, 75))
view_requests_image = ImageTk.PhotoImage(view_requests_image)
view_requests_button = tk.Button(root, command= view_requests, image= view_requests_image)

prize_image = Image.open("./assets/prizes.png")
prize_image = prize_image.resize((250, 75))
prize_image = ImageTk.PhotoImage(prize_image)
prize_button = tk.Button(root, image=prize_image, command=pick_winners) # CHANGE THIS

upcoming_event_image = Image.open("./assets/upcoming_events.png")
upcoming_event_image = upcoming_event_image.resize((270, 75))
upcoming_event_image = ImageTk.PhotoImage(upcoming_event_image)
upcoming_event = Label(root, image= upcoming_event_image, bd= 0)

login_screen = Frame(root, width= 1000, height= 500, bg= '#1c1c1c')
login_screen.place(relx= 0, rely= 0, anchor= NW)

sign_in_image = Image.open("./assets/sign_in.png")
sign_in_image = sign_in_image.resize((270, 68))
sign_in_image = ImageTk.PhotoImage(sign_in_image)
sign_in = Label(login_screen, image= sign_in_image, bd= 0)
sign_in.place(relx= .5, rely= .35, anchor= CENTER)

username_entry = ctk.CTkEntry(login_screen, bg_color= "#1C1F1F", border_width= 0, width= 200, font= ("Quicksand", 15, "bold"), placeholder_text= "username")
username_entry.place(relx= .5, rely= .5, anchor= CENTER)

password_entry = ctk.CTkEntry(login_screen, bg_color= "#1C1F1F", border_width= 0, width= 200, font= ("Quicksand", 15, "bold"), placeholder_text= "password", show= '*')
password_entry.place(relx= .5, rely= .65, anchor= CENTER)

box_image = Image.open("./assets/box.png")
box_image = box_image.resize((250, 250))
box_image = ImageTk.PhotoImage(box_image)

first_box = tk.Label(image= box_image, borderwidth= 0)
second_box = tk.Label(image= box_image, borderwidth= 0)
third_box = tk.Label(image= box_image, borderwidth= 0)
temp = student_info.find()
temp2 = login_info.find()
events = event_info.find()

dates = list()
names = list()
points = list()
x = 0
for event in events:
    dates.append(event["date"].split("/"))

for date in dates:
    date_temp = list(map(int, date))
    dates[x] = date_temp
    x+= 1

x = 0
for date in dates:
    new_date = datetime.date(date[2], date[0], date[1])
    dates[x] = new_date
    x+= 1

dates.sort()

for date in dates:
    string = date.strftime('%m/%d/%Y')
    events = event_info.find()
    for event in events:
        if string == event['date']:
            names.append(event['name'])
            points.append(event['points'])

name_label1 = ctk.CTkLabel(root, text= "", font= ("Quicksand_bold", 25, "bold"))
name_label2 = ctk.CTkLabel(root, text= "")
name_label3 = ctk.CTkLabel(root, text= "")

date_label1 = ctk.CTkLabel(root, text= "")
date_label2 = ctk.CTkLabel(root, text= "")
date_label3 = ctk.CTkLabel(root, text= "")

point_label1 = ctk.CTkLabel(root, text= "")
point_label2 = ctk.CTkLabel(root, text= "")
point_label3 = ctk.CTkLabel(root, text= "")

status_label1 = ctk.CTkLabel(root, text= "")
status_label2 = ctk.CTkLabel(root, text= "")
status_label3 = ctk.CTkLabel(root, text= "")

temp_count = 0
request = list()
def refresh_events(count, value, move, type, type2): 
    global temp_count
    global request
    request = []
    if value == True: 
        if (count+ 2 < len(dates)- 1 and move == 1) or (count -1 >= 0 and move == -1) or (move == 0):
            print(names)
            if move == 0:
                ...
            elif move == 1:
                count += 1
            else:
                count -= 1

            name_text1 = tk.StringVar()
            name_text1.set(names[count])
            name_label1.configure(text= name_text1.get())
            name_label1.place(relx = 0.2, rely = 0.25, anchor= "center")

            date_text1 = tk.StringVar()
            date_text1.set(dates[count])
            date_label1.configure(text= date_text1.get())
            date_label1.place(relx = 0.2, rely = 0.5, anchor= "center")

            point_text1 = tk.StringVar()
            point_text1.set(points[count])
            point_label1.configure(text= point_text1.get())
            point_label1.place(relx = 0.2, rely = 0.6, anchor= "center")

            if type == 1 and type2 == "attending":
                request = [name_text1.get(), date_text1.get(), "attending"]
            elif type == 1 and type2 == "participating":
                request = [name_text1.get(), date_text1.get(), "participating"]

            participating_button1.place(relx= 0.15, rely= 0.35, anchor= "center")
            attending_button1.place(relx= 0.25, rely= 0.35, anchor= "center")

            name_text2 = tk.StringVar()
            name_text2.set(names[count+ 1])
            name_label2.configure(text= name_text2.get())
            name_label2.place(relx = 0.5, rely = 0.4, anchor= "center")

            date_text2 = tk.StringVar()
            date_text2.set(dates[count+ 1])
            date_label2.configure(text= date_text2.get())
            date_label2.place(relx = 0.5, rely = 0.5, anchor= "center")

            point_text2 = tk.StringVar()
            point_text2.set(points[count+ 1])
            point_label2.configure(text= point_text2.get())
            point_label2.place(relx = 0.5, rely = 0.6, anchor= "center")

            if type == 2 and type2 == "attending":
                request = [name_text2.get(), date_text2.get(), "attending"]
            elif type == 2 and type2 == "participating":
                request = [name_text2.get(), date_text2.get(), "participating"]

            participating_button2.place(relx= 0.45, rely= 0.35, anchor= "center")
            attending_button2.place(relx= 0.55, rely= 0.35, anchor= "center")

            name_text3 = tk.StringVar()
            name_text3.set(names[count+ 2])
            name_label3.configure(text= name_text3.get())
            name_label3.place(relx = 0.8, rely = 0.4, anchor= "center")

            date_text3 = tk.StringVar()
            date_text3.set(dates[count+ 2])
            date_label3.configure(text= date_text3.get())
            date_label3.place(relx = 0.8, rely = 0.5, anchor= "center")

            point_text3 = tk.StringVar()
            point_text3.set(points[count+ 2])
            point_label3.configure(text= point_text3.get())
            point_label3.place(relx = 0.8, rely = 0.6, anchor= "center")

            if type == 3 and type2 == "attending":
                request = [name_text3.get(), date_text3.get(), "attending"]
            elif type == 3 and type2 == "participating":
                request = [name_text3.get(), date_text3.get(), "participating"]

            participating_button3.place(relx= 0.75, rely= 0.35, anchor= "center")
            attending_button3.place(relx= 0.85, rely= 0.35, anchor= "center")
            
            temp_count = count
            
            x = 0
            requests = request_info.find()
            if type > 0:
                for i in requests:
                    if i.get("student_id") == student_id and i.get("name") == request[0] and i.get("date") == request[1]:
                        x+= 1
                if x == 0:
                    temp_info = {"student_id": student_id, "name": request[0], "date": request[1], "type": request[2], "status": "pending"}
                    request_info.insert_one(temp_info)
                else:
                    print("error message")

        else:
            ...
    else:
        name_label1.place_forget()
        name_label2.place_forget()
        name_label3.place_forget()
        count = 0

forward_image = Image.open("./assets/right_arrow.png")
forward_image = forward_image.resize((50, 50))
forward_image = ImageTk.PhotoImage(forward_image)
forward = tk.Button(root, image= forward_image, command=lambda: refresh_events(temp_count, True, 1, 0, "empty"), borderwidth= 0, highlightthickness= 0, bd= 0)

backward_image = Image.open("./assets/left_arrow.png")
backward_image = backward_image.resize((50, 50))
backward_image = ImageTk.PhotoImage(backward_image)
backward = tk.Button(root, image= backward_image, command=lambda: refresh_events(temp_count, True, -1, 0, "empty"), borderwidth= 0, highlightthickness= 0, bd= 0 )

participating_image = Image.open("./assets/participating.png")
participating_image = participating_image.resize((80, 24))
participating_image = ImageTk.PhotoImage(participating_image)
participating_button1 = tk.Button(root, image= participating_image, command=lambda: refresh_events(temp_count, True, 0, 1, "participating"))
participating_button2 = tk.Button(root, image= participating_image, command=lambda: refresh_events(temp_count, True, 0, 2, "participating"))
participating_button3 = tk.Button(root, image= participating_image, command=lambda: refresh_events(temp_count, True, 0, 3, "participating"))

attending_image = Image.open("./assets/attending.png")
attending_image = attending_image.resize((80, 24))
attending_image = ImageTk.PhotoImage(attending_image)
attending_button1 = tk.Button(root, image= attending_image, command=lambda: refresh_events(temp_count, True, 0, 1, "attending"))
attending_button2 = tk.Button(root, image= attending_image, command=lambda: refresh_events(temp_count, True, 0, 2, "attending"))
attending_button3 = tk.Button(root, image= attending_image, command=lambda: refresh_events(temp_count, True, 0, 3, "attending"))

def login():
    global student_id
    temp = student_info.find()
    temp2 = login_info.find()
    events = event_info.find()

    logged_in = False

    if logged_in == False:
        for item in temp:
            if str(password_entry.get()) == str(item["_id"]) and str(username_entry.get()) == str(item["last_name"]):
                student_id = item["_id"]
                event_button.place_forget()
                add_student_button.place_forget()
                view_button.place_forget()
                login_screen.place_forget()
                label.place_forget()
                create_report_button.place_forget()
                logged_in = True

                sign_out.place(relx=0.15, rely=0.8, anchor="center")
                prize_button.place(relx= 0.5, rely= 0.8, anchor= "center")
                about_button.place(relx= 0.85, rely= 0.8, anchor= "center")
                upcoming_event.place(relx= .5, rely= .08, anchor= CENTER)

                first_box.place(relx= 0.2, rely= 0.4, anchor= "center")

                second_box.place(relx= 0.5, rely= 0.4, anchor= "center")

                third_box.place(relx= 0.8, rely= 0.4, anchor= "center")

                refresh_events(0, True, 0, 0, "empty")

                forward.place(relx= 0.965, rely= 0.4, anchor= "center")
                backward.place(relx= 0.035, rely= 0.4, anchor= "center")

    if logged_in == False:
        for item2 in temp2:
            if str(password_entry.get()) == str(item2["password"]) and str(username_entry.get()) == str(item2["username"]):
                login_screen.place_forget()
                sign_out.place(relx=0.15, rely=0.8, anchor="center")
                logged_in = True

                event_button.place(relx=0.85, rely=0.2, anchor="center")
                add_student_button.place(relx=0.15, rely=0.2, anchor="center")
                about_button.place(relx=0.85, rely=0.4, anchor="center")
                view_button.place(relx=0.85, rely=0.6, anchor="center")
                create_report_button.place(relx=0.15, rely=0.6, anchor="center")
                prize_button.place(relx=0.85, rely=0.8, anchor="center")
                upcoming_event.place(relx= .5, rely= .1, anchor= CENTER)
                label.place(relx=0.5, rely=0.5, anchor="center")
                view_requests_button.place(relx= 0.15, rely= 0.4, anchor= "center")

                upcoming_event.place_forget()

    if logged_in == False:
        if str(password_entry.get()) == "" or str(username_entry.get()) == "":
            error("Please fill out all the fields.")
        else:
            error("Incorrect username or password.")
    

login_image = Image.open("./assets/login.png")
login_image = login_image.resize((60, 60))
login_image = ImageTk.PhotoImage(login_image)
login_button = tk.Button(login_screen, image=login_image, command=login) # CHANGE THIS
login_button.place(relx=0.425, rely=0.8, anchor="center")

register_image = Image.open("./assets/register.png")
register_image = register_image.resize((60, 60))
register_image = ImageTk.PhotoImage(register_image)
register_button = tk.Button(login_screen, image=register_image, command=register) # CHANGE THIS
register_button.place(relx=0.575, rely=0.8, anchor="center")

img1 = Image.open("./assets/logo.png")
img1 = img1.resize((200, 200))
img1 = ImageTk.PhotoImage(img1)


def place_login_frame():
    first_box.place_forget()
    second_box.place_forget()
    third_box.place_forget()
    forward.place_forget()
    backward.place_forget()
    login_screen.place(relx= 0, rely= 0, anchor= NW)
    sign_out.place_forget()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    refresh_events(0, False, 0, 0, "empty")
    attending_button1.place_forget()
    attending_button2.place_forget()
    attending_button3.place_forget()
    participating_button1.place_forget()
    participating_button2.place_forget()
    participating_button3.place_forget()
    name_label1.place_forget()
    name_label2.place_forget()
    name_label3.place_forget()
    date_label1.place_forget()
    date_label2.place_forget()
    date_label3.place_forget()
    point_label1.place_forget()
    point_label2.place_forget()
    point_label3.place_forget()
    view_requests_button.place_forget()

sign_out_image = Image.open("./assets/sign_out.png")
sign_out_image = sign_out_image.resize((250, 75))
sign_out_image = ImageTk.PhotoImage(sign_out_image)
sign_out = tk.Button(root, image=sign_out_image, command= place_login_frame)



# keeps gui running
if __name__ == "__main__":
    root.mainloop()
