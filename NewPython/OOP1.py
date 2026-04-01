'''
def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")
    
def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

if __name__ == "__main__":
    main()
'''

'''
# tuple, we cannot change the item in tuple
def main():
    # name, house = get_student()
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]

if __name__ == "__main__":
    main()
'''

'''
# Using dict
def main():
    # name, house = get_student()
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")
    
def get_student():
    # student = {}
    # student["name"] = input("Name: ")
    # student["house"] = input("House: ")
    # return student
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()
'''

'''
def main():
    # name, house = get_student()
    student = get_student()
    print(f"{student.name} from {student.house}")
    
def get_student():
    # student = Student()
    # student.name = input("Name: ")
    # student.house = input("House: ")
    return student

if __name__ == "__main__":
    main()
'''

'''
class Student:
    def __init__(self, name, house): #instance method #dunder method
        self.name = name
        self.house = house

def main():
    # name, house = get_student()
    student = get_student()
    print(f"{student.name} from {student.house}")
    
def get_student():
    # student = Student()
    # student.name = input("Name: ")
    # student.house = input("House: ")
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()
'''

'''
class Student:
    def __init__(self, name, house): #instance method #dunder method
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

def main():
    # name, house = get_student()
    student = get_student()
    print(f"{student.name} from {student.house}")
    print(student)
    
def get_student():
    # student = Student()
    # student.name = input("Name: ")
    # student.house = input("House: ")
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()
'''

'''
class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus
        
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return ":)"
            case "Otter":
                return ";)"
            case "Jack Russell":
                return ":>"
            case _:
                return ":/"

def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)

if __name__ == "__main__":
    main()
'''

'''
# Introduction to Properties, attributes, decorators
class Student:
    def __init__(self, name, house):
        self.name = name
        # if we do not use the "_" here in the instance variable so this also goes through the setter and getter and check errors. so we dont need to check twice.
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @property #Use to set the Getter function
    def name(self):
        return self._name
        # The _ and __ is used for the private and super private variables python will still going to give you access to these but the conventions will suggest that dont use those in the main function because it will broke the code
    
    @name.setter #the property that I created above called name
    def name(self, name): #this also have the another argument
        if not name:
            raise ValueError("Missing name")
        self._name = name
    
    @property # Getter
    def house(self):
        return self._house
    
    @house.setter # Setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

def main():
    student = get_student()
    # student.house = "Number Four, Privet Drive"
    # student._house = "Number Four, Privet Drive" #here the _house will change the value of the variable but not use by convention
    # We can change instance variable but if we use the Getter and Setter the python can not going to let you use directly, when we again going to set or call the value it will go through the getter and setter and solve if any unwanted error occurs or input occurs
    print(student)
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()
'''