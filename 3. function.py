'''
# function 
def hello():
    print("Hello")
    
name = input("What's your name? ")
hello()
print(name)
'''

'''
# taking one parameter to the function 
def hello(to):
    print("Hello, ", to)
    
name = input("What's your name? ")
hello(name)
'''

'''
# taking one parameter to the function 
def hello(to="World"): #it will set default value if user doesnt give the value or function doesnot have the parameter it take that as the default parameter
    print("Hello,", to)
    
name = input("What's your name? ")
hello() #here is not parameter
hello(name) #here is the parameter taking empty value
'''

'''
# we can't define the function after calling it we need to define it before the calling the funciton or there is another technique 
# this is hwo you can make a main function and call it whenever you want the main code will be inside the main function /\
def main():
    name = input("What's your name? ")
    # hello() #here is not parameter
    hello(name) #here is the parameter taking empty value
    
def hello(to="World"): #it will set default value if user doesnt give the value or function doesnot have the parameter it take that as the default parameter
    print("Hello,", to)
    
main()
'''

'''
# scope refers to a variable only existing in the context in which you defined it 
# the "main" variable can not be caled in the hello function because the scope of it is in the that particular function only 
# lets learn how to use the return it will retun some string or some value back to you 
def main():
    x = int(input("what's x? "))
    print("x squared is", square(x))
    
def square(num):
    sqofnum = num*num
    return sqofnum
    
main()
'''