import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import pymongo
from pymongo import MongoClient
from matplotlib.backends.backend_pdf import PdfPages
import customtkinter as ctk


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


def create_report_all_grades(student_data):
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
        y = np.arange(len(student_indices[idx]))
        ax_all.barh(student_indices[idx], grade_values[idx], color=colors[idx], label=grade, alpha=0.6)

    ax_all.legend()
    plt.ylabel('Students')
    plt.xlabel('Points')
    plt.title('All Grades')

    plt.tight_layout()
    plt.show()

    return fig_all


def create_report_per_grade(student_data, grade):
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
    plt.show()

    return fig


def export_to_pdf(figures, root):
    with PdfPages('student_report.pdf') as pdf:
        for fig in figures:
            pdf.savefig(fig)
            plt.close(fig)

    success_window = tk.Toplevel(root)
    success_label = tk.Label(success_window, text="PDF exported successfully.")
    success_label.pack()

    def close_all_windows():
        root.destroy()
        success_window.destroy()

    success_window.protocol("WM_DELETE_WINDOW", close_all_windows)


def createReport():
    cluster = MongoClient("mongodb+srv://RRHSfbla2023:IheBcYm1ZbOEephx@fbla2023project.wdozi9i.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["RRHSfbla2023"]
    student_info = db["student_info"]

    root = tk.Tk()
    root.geometry('800x600')

    student_data = get_student_data(student_info)

    # Create a button for each grade
    for grade in range(9, 13):
        ctk.CTkButton(root, text=f"Show Grade {grade}", command=lambda grade=grade: create_report_per_grade(student_data, grade)).pack()

    # Create "Show All Grades" button
    ctk.CTkButton(root, text="Show All Grades", command=lambda: create_report_all_grades(student_data)).pack()

    # Create "Export All" button
    ctk.CTkButton(root, text="Export All to PDF", 
                  command=lambda: export_to_pdf(
                      [create_report_all_grades(student_data)] 
                      + [create_report_per_grade(student_data, grade) for grade in range(9, 13)],
                      root
                  )).pack()

    root.mainloop()


if __name__ == '__main__':
    createReport()
