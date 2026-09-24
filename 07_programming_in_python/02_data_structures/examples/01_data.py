students = [
    {"name": "Ali", "score": 82},
    {"name": "Ahsan", "score": 91},
    {"name": "Ahmed", "score": 76},
]

top_student = max(students, key=lambda student: student["score"])
print(top_student)
