'''
import random
class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
        
    def sort(self, name):
        print(name, "is in", random.choice(self.houses))
    
hat = Hat()
hat.sort("Harry")
'''

'''
import random
class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))
    
Hat.sort("Harry")
'''

'''
class Student:
    def __init__(self, name1, house1):
        self.name2 = name1
        self.house2 = house1
        
    def __str__(self):
        return f"{self.name2} from {self.house2}"
    
    @classmethod
    def get(cls):
        name3 = input("Name: ")
        house3 = input("House: ")
        return cls(name3, house3) #This will initialize the class and return what is in the str

def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()
'''