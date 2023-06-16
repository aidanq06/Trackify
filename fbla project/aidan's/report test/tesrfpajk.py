import matplotlib.pyplot as plt
#color dodgerblue
def create_report(student_data, grade):
    # Filter students of the specified grade and sort by points
    grade_data = [student for student in student_data if student['grade'] == grade]
    sorted_data = sorted(grade_data, key=lambda k: k['points'], reverse=True)
    
    # Create lists for student names and their points
    student_names = [student['name'] for student in sorted_data]
    points = [student['points'] for student in sorted_data]

    # Define plot size
    plt.figure(figsize=(10, 0.25 * len(student_names)))
    
    # Create horizontal bar chart
    bars = plt.barh(student_names, points, color='skyblue')

    # Label the bars with their exact point values
    for bar in bars:
        plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2,
                 f'{bar.get_width():.0f}', va='center')

    plt.xlabel('Points')
    plt.title(f'Grade {grade} Student Report')
    plt.grid(True)

    plt.show()

# example student data
students = [
    {'name': f'Student {i}', 'points': 100 - i, 'grade': 1 if i < 50 else 2}
    for i in range(100)
]

create_report(students, grade=1)
