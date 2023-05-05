import customtkinter as ctk
import random as rand

from popups import success, error
from main import connect_to_db

cursor = connect_to_db()

def pickWinner():
    prizes = ["free spirit gear", "a day of excused school", "free admission to all school games for a quarter", "free lunch for a week"]
    studentValues = list()
    cursor.execute("SELECT * FROM students")
    all_students = cursor.fetchall()
    pointList = list()
    maxStudents = list()
    max = all_students[0][3]
    for i in range(len(all_students)):
        pointList.append((all_students[i][3],all_students[i][4]))
        if all_students[i][3] > max:
            max = all_students[i][3]
    for i in range(len(all_students)):
        if max == all_students[i][3]:
            maxStudents.append(all_students[i])
    
    # GUI
    win = ctk.CTkToplevel()
    win.title("Winners")
    win.geometry("400x800")

    #prints the winner if there is multiple winners
    if len(maxStudents) > 1:
        Label2 = ctk.CTkLabel(win, text= "These students tied for first place: ", corner_radius=10)
        Label2.pack()
        for i in range(len(maxStudents)):
            Label = ctk.CTkLabel(win, text=f" {(maxStudents[i][0]).title()} {(maxStudents[i][1][0]).title()}. with a total of: {maxStudents[i][3]} points.", corner_radius=10)
            Label.pack()

    #prints the winner if there is only one winner
    else:
        Label3 = ctk.CTkLabel(win, text= "The student that won first place is: ", corner_radius=10)
        Label3.pack()

        Label4 = ctk.CTkLabel(win, text=f" {(maxStudents[0][0]).title()} {(maxStudents[0][1][0]).title()}. with a total of: {maxStudents[0][3]} points.", corner_radius=10)
        Label4.pack()

    try:
        #picks a random winner for each grade level
        for grade in range(9, 13):
            cursor.execute("SELECT * FROM students WHERE grade = :grade", {'grade': grade})
            gradeStudents = cursor.fetchall()
            randStudent = rand.randint(0, len(gradeStudents)-1)
            studentValues.append(gradeStudents[randStudent])
            space = ctk.CTkLabel(win, text= " ")
            space.pack()
            label5= ctk.CTkLabel(win, text= "The random winner for grade " + str(grade) + " is: ")
            label5.pack()
            label6 = ctk.CTkLabel(win, text= f" {(gradeStudents[randStudent][0]).title()} {(gradeStudents[randStudent][1][0]).title()}. with a total of: {gradeStudents[randStudent][3]} points.")
            label6.pack()  

        space1 = ctk.CTkLabel(win, text= "")
        space1.pack()
        space2 = ctk.CTkLabel(win, text= "")
        space2.pack()
        rand.shuffle(studentValues)

        if len(maxStudents) > 1:
            label7 = ctk.CTkLabel(win, text= " These students won a Pizza Party for their class: ")
            label7.pack()
            for i in range(len(maxStudents)):
                Label10 = ctk.CTkLabel(win, text=f" {(maxStudents[i][0]).title()} {(maxStudents[i][1][0]).title()}. ", corner_radius=10)
                Label10.pack()

    #prints the winner if there is only one winner
        else:
            Label11 = ctk.CTkLabel(win, text= "This student won a Pizza Party for their class: ", corner_radius=10)
            Label11.pack()

            Label12 = ctk.CTkLabel(win, text=f" {(maxStudents[0][0]).title()} {(maxStudents[0][1][0]).title()}.", corner_radius=10)
            Label12.pack()

        for i in range(len(studentValues)):
            label14 = ctk.CTkLabel(win, text="")
            label14.pack()
            label13 = ctk.CTkLabel(win, text=str(studentValues[i][0]) + " " + str(studentValues[i][1][0]) + ". wins " + prizes[i])
            label13.pack()
        


    except ValueError:
        ...