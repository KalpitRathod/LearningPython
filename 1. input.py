'''
This reference files is created by Kalpit Rathod.
'''

'''
Variable will store the values input by the user
Functions will run predefined task
Arguments is the input for the functions
When we call the variable in print it will return value
Bugs is the mistake in programming.
'''
# this is comment

# Taking the input from the input function and store it in the name variable
'''
name = input("Enter your name: ")
'''
# Now this will print the hard text
'''
print("Hello, "+name) # This will use only one argument
print("Hello,",name) # This will use two arguments
'''
# This will print the variable stored value
'''
print(name, 'This is "Comma"')
print(name, "This is \"Comma\"")
print(name, f"This is {name}") #format string
'''

# string is the array of charactors or this is the type of data in python it known as the str
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# sep is seperator, when we pass multiple arguments it will separate with the dafault space
# end is the \n means new line, dafault is the always new line

'''
name = input("Name: ").strip().title()
# Remove whitespace from str
# name = name.strip()
# name = name.capitalize() #capitalized first letter
# name = name.title() #capitalized first letter each word
print(f"This is {name}") #format string
'''

'''
# Split use name into first name and last name 
name = input("Name: ").strip().title()
first, last = name.split(" ")
print("First Name: "+first+" And Last Name: "+last)
'''