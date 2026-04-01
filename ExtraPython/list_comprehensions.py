'''
def main():
    yell("This", "is", "CS50")
    
def yell(*words):
    uppercased = [word.upper() for word in words] #list comprehensions
    print(*uppercased)
    
if __name__ == "__main__":
    main()
'''

'''
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors):
    print(gryffindor)
'''

'''
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]


def is_gryffindor(s):
    return s["house"] == "Gryffindor"


gryffindors = filter(is_gryffindor, students)

# for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
for gryffindor in gryffindors:
    print(gryffindor["name"])

'''