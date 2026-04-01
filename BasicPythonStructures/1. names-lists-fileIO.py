'''
name = input("What's your name? ")
print(f"hello, {name}")
'''

'''
names = []

# Store value in list 
for _ in range(3):
    names.append(input("What's your name? "))
    
for name in sorted(names):
    print(f"hello, {name}")
'''

'''
# 'w' will recreate the file
# 'a' will append the lines in the file
#Create the file using code
name = input("What's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
'''

'''
#Using 'with'
name = input("What's your name? ")
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
'''

'''
#Read lines from the file
with open("names.txt", "r") as file:
    lines = file.readlines()
    
for line in lines:
    print(f"Hello, {line.rstrip()}") #the print has it's own new line implementation (also can use end="")
'''

'''
#There is always a short way
with open("names.txt", "r") as file:
    for line in file:
        print("Hello,", line.rstrip())
'''

'''
# Let's Sort the names in the file
names = []

with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())
        
for name in sorted(names): #there is "reverse=True" argument
    print(f"Hello, {name}")
'''

'''
#There is always a short way
with open("names.txt", "r") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())
'''

