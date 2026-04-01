def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

'''
# for a million lines of code it will fill up the memory and processing power
def sheep(n):
    flock = []
    for i in range(n+1):
        if i == 0:
            pass
        else:
            flock.append("|Sheep|" * i)
    print(flock)
    return flock
'''

# yield ca return one iteration from loop
def sheep(n):
    for i in range(n+1):
        if i == 0:
            pass
        else:
            yield "|Sheep|" * i

if __name__ == "__main__":
    main()
