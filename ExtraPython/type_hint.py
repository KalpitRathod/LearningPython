# def meow(n: int) -> None: #type hint # mypy type_hint.py
#     for _ in range(n):
#         print("meow")
        
# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows)

def meow(n: int) -> str: #type hint
    return "meow\n" * n
        
number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")