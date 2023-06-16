import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def create_report(pdf, student_data, grade=None):
    # Filter students of the specified grade if grade is given
    if grade is not None:
        student_data = [student for student in student_data if student['grade'] == grade]
        
    sorted_data = sorted(student_data, key=lambda k: k['points'], reverse=True)
    
    # Create lists for student names and their points
    student_names = [student['name'] for student in sorted_data]
    points = [student['points'] for student in sorted_data]

    plt.figure(figsize=(10, 0.25 * len(student_names)))
    bars = plt.barh(student_names, points, color='skyblue')
    
    for bar in bars:
        plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2,
                 f'{bar.get_width():.0f}', va='center')

    plt.xlabel('Points')
    title = f'All Grades Student Report' if grade is None else f'Grade {grade} Student Report'
    plt.title(title)
    plt.grid(True)
    
    pdf.savefig()  # saves the current figure into a pdf page
    plt.close()

# example student data
students = [
    {'name': f'Student {i}', 'points': 100 - i, 'grade': (i % 4) + 1}
    for i in range(100)
]

with PdfPages('student_report.pdf') as pdf:
    create_report(pdf, students)
    for grade in range(1, 5):
        create_report(pdf, students, grade=grade)
