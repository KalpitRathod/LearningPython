# print("Hello World) # SyntexError

'''
try:
    x = int(input("What's x? "))
    # print(f"x is {x}")
except ValueError: # find what type of error could happen and than use error handling
    print("x is not an integer")
    
print(f"x is {x}") # ValueError #This will generate NameError while dealing with exceptions because x is creating valueError and will happen if put the different input data type than the numbers
'''

'''
# Solving above problem if the except alse have the error than it will run the else code
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
'''

'''
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break
    
print(f"x is {x}")
'''

'''
def get_int():
    while True:
        try: # this is the function{}, try is a statment
            x = int(input("What's x? ")) # we can direct return this also
        except ValueError:
            print("x is not an integer")
        else:
            break # here i can return x also. it will break and return the value.
    return x

def main():
    x = get_int()
    print(f"x is {x}")

main()
'''

'''
# Using the pass
def get_int():
    while True:
        try: # this is the function{}, try is a statment
            x = int(input("What's x? ")) # we can direct return this also
            return x
        except ValueError:
            pass

def main():
    x = get_int()
    print(f"x is {x}")

main()
'''

# if we want to make more dynamic prompt that user will ask than we can do this
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")
    
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
        
main()
# we can use raise to raise the exception