def main():
    hello("Mars")
    goodbye("Earth")

def hello(name):
    print(f"Hello, {name}")
    
def goodbye(name):
    print(f"Goodbye, {name}")
    
if __name__ == "__main__": #use name when we only want to use the main function from the command line not from library
    main()