'''
#Part of Way 3
students = []

with open("names.csv") as file:
    for line in file:
        
        #Way 1
        # row = line.rstrip().split(",")
        # print(f"{row[0]} is in {row[1]}")
        
        #Way 2
        # name, house = line.rstrip().split(",")
        # print(f"{name} is in {house}")
        
        #Way 3 for to sort
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")
        
#Part of Way 3 for to sort
for student in sorted(students):
    print(student)
'''

'''
#Sort by the dist only for name and print
students = []

with open("names.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        
        #Way 1 to make dist
        # student = {}
        # student["name"] = name
        # student["house"] = house
        
        #Way 2 to make dist
        student = {"name": name, "house": house}
        
        students.append(student)

# def get_name(student):
#     return student["name"]

# for student in sorted(students, key=get_name):
#     print(f"{student['name']} is in {student['house']}")
    
#There is a another way to write the function in this situation
for student in sorted(students, key=lambda student: student["name"]): #by using lambda function
    print(f"{student['name']} is in {student['house']}")
'''

'''
#Using CSV
import csv
#Sort by the dist only for name and print
students = []

with open("names.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})
    
for student in sorted(students, key=lambda student: student["name"]): #by using lambda function
    print(f"{student['name']} is in {student['home']}")
'''

'''
# Using Dict Reader
import csv
#Sort by the dist only for name and print
students = []

with open("names.csv") as file:
    reader = csv.DictReader(file) #Dict Reader
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})
    
for student in sorted(students, key=lambda student: student["name"]): #by using lambda function
    print(f"{student['name']} is in {student['home']}")
'''

'''
#Using Write in CSV
import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name,home])
'''

#Using Dict Write in CSV (Order does not matter)
import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})