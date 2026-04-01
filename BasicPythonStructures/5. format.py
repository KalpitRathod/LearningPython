'''
name = input("What's your name? ").strip()
if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"hello, {name}")
'''

'''
import re
name = input("What's your name? ").strip()
matches = re.search(r"^(.+), ?(.+)$", name)
if matches:
    # last, first = matches.groups()
    # last = matches.group(1)
    # first = matches.group(2)
    # name = f"{first} {last}"
    name = f"{(matches.group(2)).strip()} {(matches.group(1)).strip()}"
print(f"hello, {name}")
'''

import re
name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), ?(.+)$", name): #":=" it will ask and assign both in same expression(Wolris)
    name = f"{(matches.group(2)).strip()} {(matches.group(1)).strip()}"
print(f"hello, {name}")