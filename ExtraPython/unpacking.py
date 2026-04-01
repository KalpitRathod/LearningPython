'''
first, last = input("What's your name?").split(" ")
print(f"hello, {first}")
'''

'''
coins = [100, 50, 25]

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

print(total(*coins), "Knuts")
'''

'''
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50, "knuts": 25}

# print(total(galleons=100, sickles=50, knuts=25), "Knuts")
# print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")
print(total(**coins), "Knuts") #double * can be used for dict
'''

'''
import sys
def f(*args, **kwargs):
    print("Positional:", args)
    print("Named:", kwargs)
    
f(100, 50, 25, galleons = 50)

# print(*object, sep=' ', end='\n', file=sys.stdout, flush=False)

# def print(*objects, sep=' ', end='\n', ...):
#     for object in objects:
#         ...
'''