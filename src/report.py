import customtkinter as ctk
import matplotlib.pyplot as plt
from tkinter import *

from popups import error
from main import connect_to_db

cursor = connect_to_db()

def report():
    def destroyGui():
        dialog_box.destroy()

    def save_inputs():
        try:
            dialog_box.destroy()
            choice = grade_level.get()
            cursor.execute("SELECT * FROM students WHERE grade = :grade", {'grade': choice})
            fetch = cursor.fetchall()
            points = list()
            name = list()
            for i in range(len(fetch)):
                points.append(fetch[i][3])
                name.append(f"{fetch[i][0]} {(fetch[i][1][0]).title()}.")
            name2=list()
            for i in range(len(name)):
                name2.append(f"{name[i]} ({points[i]} points)")
            if points==[] and name==[]:
                error(f"There currently isn't any data for grade {choice}.")
            else:
                plt.rcParams["figure.figsize"] = (15,5)
                plt.barh(name2,points,color="royalblue")

                #plt.plot(range(len(data)), data,"r+")
                plt.savefig(f"QuarterlyG{choice}.pdf",format="pdf")

                plt.title(f'Quarterly Points (Grade {choice})', fontweight="bold")

                plt.ylabel('Students', fontweight="bold")
                plt.xlabel('Points', fontweight="bold")

                plt.show()
        except TclError: # didnt select a grade
            error("Please select a grade.")

    #GUI    
    dialog_box = ctk.CTkToplevel()
    dialog_box.title("Dialog Box")
    dialog_box.geometry("400x100")
    dialog_box.resizable(False,False)

    #dropdown menu for grade selection
    dropdown = ctk.CTkLabel(dialog_box, text="Select which grade level's quarterly report you would like to view.")
    dropdown.pack()
    grade_level = ctk.IntVar(dialog_box)
    grade_level.set("Select a grade.")
    dropdown = ctk.CTkComboBox(master=dialog_box, values=["9", "10", "11", "12"], variable=grade_level)
    dropdown.pack()

    # Submit grade button
    save_button = ctk.CTkButton(dialog_box, text="Submit", command=save_inputs)
    save_button.place(relx=0.75,rely=0.75,anchor=CENTER)

    #quit the view students GUI
    save_button = ctk.CTkButton(dialog_box, text="Quit", command=destroyGui)
    save_button.place(relx=0.25,rely=0.75,anchor=CENTER)
