import matplotlib.pyplot as plt
import numpy as np

def create_report(student_data):
    sorted_data = sorted(student_data, key=lambda k: (k['grade'], -k['points']))
    
    grades = ['Grade 1', 'Grade 2', 'Grade 3', 'Grade 4']
    grade_values = [[], [], [], []]
    student_indices = [[], [], [], []]

    for student in sorted_data:
        grade_values[student['grade']-1].append(student['points'])
        student_indices[student['grade']-1].append(student['name'])

    fig, ax = plt.subplots()

    colors = ['blue', 'green', 'red', 'purple']
    for idx, grade in enumerate(grades):
        x = np.arange(len(student_indices[idx]))
        ax.scatter(x, grade_values[idx], color=colors[idx], label=grade, alpha=0.6)

    ax.legend()
    plt.ylabel('Points')
    plt.title('Student Report')
    plt.show()


students = [
    {'name': 'Student 1', 'points': 90, 'grade': 1},
    {'name': 'Student 2', 'points': 85, 'grade': 1},
    {'name': 'Student 3', 'points': 91, 'grade': 2},
    {'name': 'Student 4', 'points': 82, 'grade': 2},
    {'name': 'Student 5', 'points': 95, 'grade': 3},
    {'name': 'Student 6', 'points': 89, 'grade': 3},
    {'name': 'Student 7', 'points': 88, 'grade': 4},
    {'name': 'Student 8', 'points': 92, 'grade': 4},
    # add as many students as needed
]

create_report(students)
