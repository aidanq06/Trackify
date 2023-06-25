import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from pymongo import MongoClient
from matplotlib.backends.backend_pdf import PdfPages
import customtkinter as ctk

import subprocess
from popups import error


def get_student_data(student_info):
    # Fetch all students from the database
    students = list(student_info.find())

    # For each student in the database, create a dictionary with their abbreviated name, points, grade, and ID
    students = [
        {
            'name': f'{student["first_name"]} {student["last_name"][0]}. ({student["_id"]})', 
            'points': student['point'], 
            'grade': student['grade']
        } 
        for student in students
    ]

    return students

import numpy as np

import numpy as np

def create_report_all_grades(student_data, show_plot=True):
    # Plot data for all grades combined
    sorted_data = sorted(student_data, key=lambda k: (k['grade'], -k['points']))
    grades = ['Grade 9', 'Grade 10', 'Grade 11', 'Grade 12']
    grade_values = [[], [], [], []]
    student_indices = [[], [], [], []]

    for student in sorted_data:
        grade_values[student['grade']-9].append(student['points'])
        student_indices[student['grade']-9].append(student['name'])

    fig_all, ax_all = plt.subplots()

    colors = ['blue', 'green', 'red', 'purple']
    for idx, grade in enumerate(grades):
        y = np.ones(len(student_indices[idx])) * idx  # Set the y-axis values to be the grade index
        x = grade_values[idx]
        ax_all.errorbar(x, y, xerr=np.std(x), fmt='o', color=colors[idx], label=grade, alpha=0.6)

    ax_all.legend()
    plt.yticks(np.arange(len(grades)), grades)  # Set the y-axis tick labels to be the grade names
    plt.xlabel('Points')
    plt.title('Grade Averages')

    plt.tight_layout()
    if show_plot:
        plt.show()

    return fig_all



def create_report_per_grade(student_data, grade, show_plot=True):
    # Filter the students belonging to the selected grade
    filtered_data = [student for student in student_data if student['grade'] == grade]
    
    # Sort students by their points
    sorted_data = sorted(filtered_data, key=lambda k: -k['points'])

    # Get the points and names of the students
    points = [student['points'] for student in sorted_data]
    names = [student['name'] for student in sorted_data]

    fig, ax = plt.subplots()
    bars = ax.barh(names, points, color='blue', alpha=0.6)

    for bar, point in zip(bars, points):
        ax.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{point}',
                ha='left', va='center', color='black', fontsize=8)

    plt.xlabel('Points')
    plt.title(f'Grade {grade}')

    plt.tight_layout()

    if show_plot:
        plt.show()

    return fig


def export_to_pdf(figures, root1):
    filename='student_report.pdf'
    with PdfPages(filename) as pdf:
        for fig in figures:
            pdf.savefig(fig)
            plt.close(fig)


    # Open the file location in the file explorer
    try:
        subprocess.run(['explorer', '/select,', filename])  # For Windows
    except FileNotFoundError:
        try:
            subprocess.run(['xdg-open', '--reveal', filename])  # For Linux
        except FileNotFoundError:
            error("Could not open file location.", root=root1)
            return


    new_window = tk.Toplevel()
    new_window.geometry("+750+500")
    new_window.title("PDF Export Successful")
    new_window.configure(bg='#1c1c1c')
    new_window.grab_set()
    new_window.resizable(False,False)

    label = tk.Label(new_window, text="PDF Export Successful!", font=("Quicksand", 25), bg='#1c1c1c', fg='white',padx=20,pady=20)
    label.pack(pady=10)

    def close_all_windows():
        root1.destroy()
        new_window.destroy()

    new_window.protocol("WM_DELETE_WINDOW", close_all_windows)


def createReport(root):
    cluster = MongoClient("mongodb+srv://RRHSfbla2023:IheBcYm1ZbOEephx@fbla2023project.wdozi9i.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["RRHSfbla2023"]
    student_info = db["student_info"]

    root1 = tk.Frame(root, height=500, width=1000, bg="#1c1c1c")
    root1.place(relx=0, rely=0, anchor="nw")

    student_data = get_student_data(student_info)

    # Add a title label
    title_label = tk.Label(root1, text="create report", font=("Quicksand", 30), bg="#1c1c1c", fg="white")
    title_label.place(relx=0.5, rely=0.05, anchor="center")

    # Create a button for each grade
    for idx, grade in enumerate(range(9, 13)):
        button = ctk.CTkButton(root1, height=45, width=500, text=f"show grade {grade}", font=("Quicksand", 20), fg_color="white", text_color="#1c1c1c",
                               command=lambda grade=grade: create_report_per_grade(student_data, grade))
        button.place(relx=0.5, rely=0.175 + (idx * 0.12), anchor="center")

    # Create "Show All Grades" button
    show_all_button = ctk.CTkButton(root1, height=45, width=500, text="show all grades", font=("Quicksand", 20), fg_color="white", text_color="#1c1c1c",
                                    command=lambda: create_report_all_grades(student_data))
    show_all_button.place(relx=0.5, rely=0.175 + (4 * 0.12), anchor="center")

    # Create "Export All" button
    export_button = ctk.CTkButton(root1, height=45, width=500, text="export all to pdf", font=("Quicksand", 20), fg_color="white", text_color="#1c1c1c",
                                  command=lambda: export_to_pdf(
                                      [create_report_all_grades(student_data, show_plot=False)]
                                      + [create_report_per_grade(student_data, grade, show_plot=False) for grade in range(9, 13)],
                                      root1
                                  ))
    
    export_button.place(relx=0.5, rely=0.175 + (5 * 0.12), anchor="center")
    

    exit_button = ctk.CTkButton(root1, height=45, width=500, text="exit", font=("Quicksand", 20), fg_color="white", text_color="#1c1c1c",
                                  command=root1.destroy)
    exit_button.place(relx=0.5, rely=0.175 + (6 * 0.12), anchor="center")

    root1.mainloop()



if __name__ == '__main__':
    createReport()
