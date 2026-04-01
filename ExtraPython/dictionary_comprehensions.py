'''
students = ["Hermione", "Harry", "Ron"]

gryffindor = []

for student in students:
    gryffindor.append({"name": student, "house": "Gryffindor"})
    
print(gryffindor)
'''

'''
students = ["Hermione", "Harry", "Ron"]

gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
    
print(gryffindors)
'''

'''
students = ["Hermione", "Harry", "Ron"]

gryffindors = {student: "Gryffindor" for student in students}
    
print(gryffindors)
'''

'''
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i, students[i])
'''

'''
#enumerate
students = ["Hermione", "Harry", "Ron"]

for i, student in enumerate(students):
    print(i+1, student)
'''
