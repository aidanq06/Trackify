class student():
 def __init__(self, first, last, grade):
    self.first = first
    self.last = last
    self.grade = grade
    
input1 = input("first")
input2 = input("last")
input3 = input("grade")

new_student = student(input1, input2, input3)

print(new_student.first)
print(new_student.last)
print(new_student.grade)
print(new_student)