def main():
    # print_column(3)
    print_square(3)
    
def print_column(height):
    # for _ in range(height):
    #     print("#")
    print("#\n" * height, end="")
        
def print_row(width):
    print("?" * width)
    
def print_square(size):
    
    #Repeating the printing row size times
    for i in range(size):
        #Printing the row as given size
        for j in range(size):
            print("#", end="")
        #After printing the row start printing again from the new line
        print() # print("\n", end="")
        
    # Different way
    # for i in range(size):
    #     print("#" * size)

main()