# Calculator
'''
x = 1
y = 1

z = x+y

print(z)
'''

'''
we can debug if user inputed other than integer
x = input("What's x? ")
y = input("What's y? ")

z = int(x) + int(y) #input will take all data in string and we need to convert it to the number

print(z)
'''

'''
# expect what will we have 
x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)
'''

# one line code 
# print(int(input("What's x? ")) + int(input("What's y? ")))

'''
# float 
z = round(float(input("What's x? ")) + float(input("What's y? "))) #we can round the float value[round(number[, ndigits])]
print(f"{z:,}") #This is to format the output
'''

'''
# Different operators 
x = float(input("What's x: "))
y = float(input("What's y: "))
z1 = round(x/y,2)
z2 = x/y
print(z1, z2)
print(f"{z2:.2f}") #this will format the until to 2 digit with format string
'''