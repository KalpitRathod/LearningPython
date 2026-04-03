# 🐍 Standard Python — Deep Reference Notes

> Personal study notes by **Kalpit Rathod** covering Python from fundamentals to OOP.
> Each section explains the *why* + the *how*, with code straight from the source files.

---

## 📁 Repository Map

```
stdPython/
├── Start_Python/           # Core language fundamentals (numbered 1–18)
├── BasicPythonStructures/  # File I/O, CSV, Regex, PIL, Unit Testing
├── ExtraPython/            # Functional Python: comprehensions, generators, sets, scope
└── NewPython/              # Object-Oriented Programming (4 progressive files)
```

---

# MODULE 1 — Start_Python

## 1. Strings & Variables (`1. str.py`)

### Concepts

- A **variable** is a named container that stores a value.
- A **string** (`str`) is a sequence of characters. Python treats everything from `input()` as a string.
- **f-strings** (`f"..."`) let you embed variable values directly inside a string using `{}`.
- Strings have built-in **methods** — functions that live on the string object itself.

### Code

```python
# input() always returns a str
name = input("Enter your name: ")

# Three ways to print with a variable
print("Hello, " + name)         # concatenation (only works str + str)
print("Hello,", name)           # comma adds automatic space
print(f"Hello, {name}")         # f-string — cleanest approach

# String methods — chained together
name = input("Name: ").strip().title()
# .strip()      → removes leading/trailing whitespace
# .capitalize() → capitalizes first letter only
# .title()      → capitalizes first letter of EACH word
# .upper()      → all uppercase
# .lower()      → all lowercase

# Splitting a string
first, last = name.split(" ")   # split by space, unpack into two vars
print("First:", first, "Last:", last)
```

### print() signature
```
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
  sep  → what to put between multiple arguments (default: space)
  end  → what to add after the last item (default: newline \n)
```

---

## 2. Math & Numbers (`2. math.py`)

### Concepts

- `input()` always returns a **string**. You must cast to `int` or `float` explicitly.
- `int` — whole numbers. `float` — decimal numbers.
- `round(number, ndigits)` — rounds to N decimal places.
- Format specifiers inside f-strings control how numbers are displayed.

### Code

```python
# Type conversion (casting)
x = int(input("What's x? "))    # str → int
y = float(input("What's y? "))  # str → float

# Arithmetic operators
# +   addition
# -   subtraction
# *   multiplication
# /   division (always returns float)
# //  integer (floor) division
# %   modulo (remainder)
# **  exponentiation

# Round a float result
z = round(3.14159, 2)   # → 3.14
z = round(x / y)        # round to nearest integer

# Format specifiers in f-strings
pi = 3.14159
print(f"{pi:.2f}")      # → 3.14       (2 decimal places)
print(f"{1000000:,}")   # → 1,000,000  (comma separator)
```

---

## 3. Functions (`3. function.py`)

### Concepts

- A **function** is a reusable named block of code. Defined with `def`.
- **Parameters** = variables listed in the function definition.
- **Arguments** = values you pass when calling the function.
- **Default parameters** = fallback values if caller doesn't provide one.
- **Scope** = where a variable is visible. Variables inside a function only exist inside it.
- **Return** = send a value back to whoever called the function.
- The `main()` pattern ensures functions are defined before you use them.

### Code

```python
# Basic function
def hello():
    print("Hello")

hello()   # call it

# ---

# Function with a parameter
def hello(to):
    print("Hello,", to)

hello("Kalpit")

# ---

# Default parameter (used when no argument is passed)
def hello(to="World"):
    print("Hello,", to)

hello()           # → Hello, World
hello("Kalpit")   # → Hello, Kalpit

# ---

# The main() pattern — safely call functions defined later
def main():
    name = input("Name? ")
    hello(name)

def hello(to="World"):
    print("Hello,", to)

main()   # Python reads all defs first, then runs this

# ---

# Returning a value from a function
def main():
    x = int(input("x? "))
    print("x squared is", square(x))

def square(num):
    return num * num   # sends value back to the caller

main()
```

> **Scope rule**: a variable created inside `square()` does not exist in `main()` and vice versa.

---

## 4. Conditionals (`4. conditions.py`)

### Concepts

- Python evaluates boolean expressions to `True` or `False`.
- `if / elif / else` — only one branch runs.
- Chain comparisons Pythonically: `90 <= score <= 100`.
- **Logical operators**: `and`, `or`, `not`.
- **Ternary (inline if)**: `value_if_true if condition else value_if_false`.

### Code

```python
x = int(input("x? "))
y = int(input("y? "))

# Full if/elif/else
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x equals y")

# Logical operators
if x < y or x > y:
    print("not equal")

if x >= 0 and x <= 100:
    print("in range")

# Pythonic range check
if 0 <= x <= 100:   # works! Python supports chained comparisons
    print("in range")
```

**Grade example (chained elif)**:
```python
score = int(input("Score: "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
```

**Ternary expression**:
```python
def is_even(n):
    return n % 2 == 0        # returns True or False directly

# ternary: one-liner conditional
print("Even") if is_even(x) else print("Odd")
```

---

## 5. Match Statement (`7. house.py`)

### Concept

`match` (Python 3.10+) is like a cleaner `switch` statement. Use `|` to match multiple values in one case. `case _:` is the default/catch-all.

### Code

```python
name = input("Name? ")

# Verbose version (lots of elif)
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

# Clean version with match
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:               # default case (like else)
        print("Who?")
```

---

## 6. Loops (`8. cat-loop.py`, `11. loop-printing.py`)

### Concepts

- **`while` loop** — keep going as long as a condition is True. Risk of infinite loop.
- **`for` loop** — iterate over a sequence a known number of times.
- `range(n)` produces integers 0, 1, … n-1.
- Use `_` as the loop variable when you don't need the value (throwaway).
- `break` — exit the loop immediately.
- `continue` — skip to next iteration.
- Nested loops = loop inside a loop (for grids/2D printing).

### Code

```python
# while loop — count down
i = 3
while i != 0:
    print("meow")
    i -= 1

# while loop — count up
i = 0
while i < 3:
    print("meow")
    i += 1

# for loop with range
for i in range(3):      # i = 0, 1, 2
    print("meow")

for _ in range(3):      # _ means "I don't need the index"
    print("meow")

# String repetition shortcut
print("meow\n" * 3, end="")

# Validate input, then loop
while True:
    n = int(input("n? "))
    if n > 0:
        break           # exits the while True loop

for _ in range(n):
    print("meow")

# Refactored into functions
def main():
    meow(get_number())

def get_number():
    while True:
        n = int(input("n? "))
        if n > 0:
            return n    # return also exits the loop

def meow(n):
    for _ in range(n):
        print("meow")

main()
```

**Nested loops (print a square)**:
```python
def print_square(size):
    for i in range(size):          # each row
        for j in range(size):      # each column
            print("#", end="")     # no newline between columns
        print()                    # newline after each row

# Shorter:
    for i in range(size):
        print("#" * size)
```

---

## 7. Lists (`9. list-hogwards.py`)

### Concepts

- A **list** is an ordered, mutable (changeable) collection. Uses `[]`.
- Elements can be any type: strings, ints, dicts, even other lists.
- Access by **index** (0-based). Negative index counts from the end: `list[-1]` = last element.
- Common methods: `.append()`, `.remove()`, `.pop()`, `.sort()`, `.reverse()`.
- `sorted(list)` returns a **new** sorted list; `list.sort()` sorts in place.

### Code

```python
students = ["Hermione", "Harry", "Ron"]

print(students)          # ['Hermione', 'Harry', 'Ron']
print(students[0])       # Hermione
print(students[-1])      # Ron (last)

# Iterate
for student in students:
    print(student)

# Iterate with index
for i in range(len(students)):
    print(i, students[i])

# Better: use enumerate
for i, student in enumerate(students):
    print(i + 1, student)

# Build a list from input
names = []
for _ in range(3):
    names.append(input("Name? "))

for name in sorted(names):    # sorted doesn't mutate original
    print(f"Hello, {name}")
```

---

## 8. Dictionaries (`10. datatype-dict.py`)

### Concepts

- A **dict** is an unordered mapping of **key → value** pairs. Uses `{}`.
- Keys must be unique and immutable (strings, ints, tuples).
- Access by key: `d["key"]`. KeyError if key doesn't exist.
- Use `.get("key", default)` to avoid KeyError.
- Lists of dicts = the standard way to store tabular data in Python.

### Code

```python
# Simple dict: name → house
students = {
    "Hermione": "Gryffindor",
    "Harry":    "Gryffindor",
    "Ron":      "Gryffindor",
    "Draco":    "Slytherin",
}

print(students["Hermione"])           # Gryffindor

for student in students:              # iterates over KEYS
    print(student, students[student], sep=", ")

# ---

# List of dicts — best for structured records
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry",    "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron",      "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco",    "house": "Slytherin",  "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")

# Sort list of dicts by a key
sorted_students = sorted(students, key=lambda s: s["name"])
```

---

## 9. Exception Handling (`12. Exceptions.py`)

### Concepts

- **Exceptions** = runtime errors (things that go wrong while the program runs).
- `try / except` lets you catch errors and handle them gracefully instead of crashing.
- `else` block runs only if **no** exception occurred in `try`.
- `pass` — silently do nothing (absorb the exception and retry).
- `raise` — manually throw an exception with a message.
- Always catch the **specific** exception type, not bare `except:`.

### Code

```python
# Basic try/except
try:
    x = int(input("x? "))
except ValueError:
    print("x is not an integer")

# try / except / else
try:
    x = int(input("x? "))
except ValueError:
    print("Not a number")
else:
    print(f"x is {x}")    # only runs if try succeeded

# Loop until valid input
while True:
    try:
        x = int(input("x? "))
    except ValueError:
        print("Try again")
    else:
        break

# Refactored as a function
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))   # return exits the loop too
        except ValueError:
            pass    # silently retry

x = get_int("What's x? ")
print(f"x is {x}")

# raise — throw your own exception
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
```

---

## 10. Modules & Packages (`13. modules.py`, `16. packages.py`)

### Concepts

- A **module** is a `.py` file you import to reuse code.
- Python's **standard library** ships with hundreds of modules (`random`, `sys`, `os`, `math`, `csv`, `re`, `json`, etc.).
- `import module` — imports the whole module; prefix everything with `module.`.
- `from module import name` — imports one thing; use it directly without prefix.
- A **package** is a folder of modules with an `__init__.py`.

### Code

```python
import random

coin = random.choice(["heads", "tails"])    # random.choice
number = random.randint(1, 10)              # random.randint

cards = ["jack", "queen", "king"]
random.shuffle(cards)                        # shuffles in-place
for card in cards:
    print(card)

# Selective import (no prefix needed)
from random import choice, shuffle

coin = choice(["heads", "tails"])
```

---

## 11. Command-Line Arguments (`15. command-linearguments.py`)

### Concepts

- `sys.argv` is a **list** of strings representing what the user typed in the terminal.
- `sys.argv[0]` = the script name itself.
- `sys.argv[1]` = first user argument, `sys.argv[2]` = second, etc.
- `sys.exit(message)` prints the message to stderr and exits with error code 1.
- `argparse` is the professional way to handle complex CLI flags.

### Code

```python
import sys

# Basic: access argument
print("Hello,", sys.argv[1])    # IndexError if nothing passed!

# Safe version with length check
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("Hello,", sys.argv[1])

# Handle multiple arguments (slice from index 1)
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for name in sys.argv[1:]:        # [1:] skips the script name
    print("Hello,", name)
```

**With `argparse`** (much cleaner for real tools):
```python
import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="Number of times to meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")

# Usage: python meow.py -n 5
# Also auto-generates: python meow.py --help
```

---

## 12. APIs (`17. APIS.py`)

### Concepts

- An **API** (Application Programming Interface) lets you request data from a web service.
- `requests.get(url)` sends an HTTP GET request and returns a Response object.
- `.json()` on the response parses the JSON body into a Python dict/list.
- `json.dumps(data, indent=2)` pretty-prints any Python object as formatted JSON.

### Code

```python
import json, requests, sys

if len(sys.argv) != 2:
    sys.exit("Usage: APIS.py <search_term>")

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1]
)

# See the raw JSON (useful for exploring)
print(json.dumps(response.json(), indent=2))

# Extract just track names
data = response.json()
for result in data["results"]:
    print(result["trackName"])
```

---

# MODULE 2 — BasicPythonStructures

## 1. File I/O (`1. names-lists-fileIO.py`)

### Concepts

- `open(filename, mode)` opens a file. Always use `with` — it auto-closes the file even on error.
- Modes: `"r"` read, `"w"` write (overwrites!), `"a"` append (adds to end).
- `.read()` — entire file as one string.
- `.readlines()` — list of lines (each includes `\n`).
- Iterating directly over the file object is the most memory-efficient way.
- `.rstrip()` strips trailing whitespace/newline from each line.

### Code

```python
# Write: append to file
name = input("Name? ")
with open("names.txt", "a") as file:
    file.write(f"{name}\n")

# Read: iterate line by line (memory efficient)
with open("names.txt", "r") as file:
    for line in file:
        print("Hello,", line.rstrip())    # rstrip removes \n

# Read: collect, then sort, then print
names = []
with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello, {name}")

# Shortcut: sort while reading
with open("names.txt", "r") as file:
    for line in sorted(file):
        print("Hello,", line.rstrip())
```

> **Why `with`?** It uses the context manager protocol — guarantees `file.close()` is called even if an exception happens inside the block.

---

## 2. CSV Files (`2. students-csv.py`)

### Concepts

- CSV = Comma-Separated Values. A plain text table format.
- Python's `csv` module handles quoting, commas inside fields, and line endings automatically.
- `csv.reader` — iterates rows as **lists**.
- `csv.DictReader` — iterates rows as **dicts** (first row = header = keys). Preferred.
- `csv.writer` / `csv.DictWriter` for writing.
- `lambda` is an anonymous one-liner function, often used as a sort key.

### Code

```python
import csv

# Manual parsing (fragile — breaks if field contains comma)
with open("names.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")

# Using csv.reader
with open("names.csv") as file:
    for name, house in csv.reader(file):
        print(f"{name} is in {house}")

# Using csv.DictReader (best — header row becomes keys)
students = []
with open("names.csv") as file:
    for row in csv.DictReader(file):       # row is a dict
        students.append({"name": row["name"], "house": row["house"]})

# Sort by name using lambda
for s in sorted(students, key=lambda s: s["name"]):
    print(f"{s['name']} is in {s['house']}")

# Writing with csv.writer (order matters)
with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, house])

# Writing with csv.DictWriter (order doesn't matter)
with open("students.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
```

> **`newline=""`** in write mode prevents double line endings on Windows.

---

## 3. Regular Expressions (`4. regexes.py`)

### Concepts

- A **regex** is a pattern for matching text. Python's `re` module provides this.
- `re.search(pattern, string, flags)` — finds **first** match anywhere in string. Returns a Match object or `None`.
- `re.fullmatch(pattern, string)` — entire string must match.
- Patterns use special characters (metacharacters):

| Pattern | Meaning |
|---------|---------|
| `.` | Any character except newline |
| `*` | 0 or more of preceding |
| `+` | 1 or more of preceding |
| `?` | 0 or 1 of preceding |
| `{m}` | Exactly m repetitions |
| `{m,n}` | Between m and n repetitions |
| `^` | Start of string |
| `$` | End of string |
| `[abc]` | Any of a, b, or c |
| `[^abc]` | Anything except a, b, or c |
| `\w` | Word char: `[a-zA-Z0-9_]` |
| `\d` | Digit: `[0-9]` |
| `\s` | Whitespace (space, tab, newline) |
| `\W \D \S` | NOT word/digit/whitespace |
| `A\|B` | A or B |
| `(...)` | Capturing group |
| `(?:...)` | Non-capturing group |

**Flags**: `re.IGNORECASE` (case-insensitive), `re.MULTILINE`, `re.DOTALL`

### Code

```python
import re

email = input("Email? ").strip()

# Simple: must have exactly one @
if "@" in email:
    print("Valid (basic check)")

# Better: use regex
# \w+   → one or more word chars (username)
# @     → literal @
# \w+   → domain name
# \.    → literal dot (. needs escaping)
# (edu|com|gov|net) → one of these TLDs
if re.search(r"^\w+@\w+\.(edu|com|gov|net)$", email):
    print("Valid")
else:
    print("Invalid")

# Even better: handle dots in username, case-insensitive
if re.search(r"^(\w)+(\.)?@(\w+\.)?\w+\.(edu|com|gov|net)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

# Extracting matched groups
match = re.search(r"^(\w+)@(\w+)\.(\w+)$", email)
if match:
    print("Username:", match.group(1))
    print("Domain:",   match.group(2))
    print("TLD:",      match.group(3))
```

---

## 4. Unit Testing (`test_cal.py`, `test_hello.py`)

### Concepts

- **Unit testing** = writing small tests to verify individual functions work correctly.
- `pytest` discovers and runs all files named `test_*.py` or `*_test.py`.
- A test function must start with `test_`.
- Use `assert expected == actual` — if False, pytest marks the test as FAILED.
- Test edge cases: zero, negative, boundary values, type errors.

### Code

```python
# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

```python
# test_cal.py
import calculator

def test_add_positive():
    assert calculator.add(2, 3) == 5

def test_add_negative():
    assert calculator.add(-1, -1) == -2

def test_add_zero():
    assert calculator.add(0, 5) == 5

def test_subtract():
    assert calculator.subtract(10, 4) == 6
```

```bash
# Run all tests
pytest test_cal.py

# Verbose output
pytest -v test_cal.py
```

---

# MODULE 3 — ExtraPython

## 1. List Comprehensions (`list_comprehensions.py`)

### Concept

A compact one-line way to build a list. Replaces a `for` loop + `.append()` pattern. Can include an optional `if` filter.

**Syntax**: `[expression for item in iterable if condition]`

### Code

```python
# Loop version (verbose)
words = ["This", "is", "CS50"]
uppercased = []
for word in words:
    uppercased.append(word.upper())

# List comprehension (concise)
uppercased = [word.upper() for word in words]
print(*uppercased)    # unpack list into print (space-separated)

# With filter
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry",    "house": "Gryffindor"},
    {"name": "Ron",      "house": "Gryffindor"},
    {"name": "Draco",    "house": "Slytherin"},
]

# Get names of Gryffindor students only
gryffindors = [s["name"] for s in students if s["house"] == "Gryffindor"]

for name in sorted(gryffindors):
    print(name)

# Using filter() + lambda (same result, lazy evaluation)
gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)
for s in gryffindors:
    print(s["name"])
```

---

## 2. Dictionary Comprehensions (`dictionary_comprehensions.py`)

### Concept

Same idea as list comprehensions but builds a dict: `{key: value for item in iterable}`

### Code

```python
students = ["Hermione", "Harry", "Ron"]

# Loop version
gryffindor = []
for student in students:
    gryffindor.append({"name": student, "house": "Gryffindor"})

# List comprehension (list of dicts)
gryffindors = [{"name": s, "house": "Gryffindor"} for s in students]

# Dict comprehension (name → house mapping)
gryffindors = {student: "Gryffindor" for student in students}
# → {"Hermione": "Gryffindor", "Harry": "Gryffindor", "Ron": "Gryffindor"}

# enumerate — get both index AND value
for i, student in enumerate(students):
    print(i + 1, student)
# → 1 Hermione
# → 2 Harry
# → 3 Ron
```

---

## 3. `map()` Function (`map_function.py`)

### Concept

`map(function, iterable)` applies a function to **every element** of an iterable. Returns a lazy **map object** (evaluated only when iterated). Avoids writing a for loop.

### Code

```python
words = ["This", "is", "CS50"]

# Loop version
uppercased = []
for word in words:
    uppercased.append(word.upper())

# map version — more functional, no side effects
uppercased = map(str.upper, words)   # str.upper is a reference to the method
print(*uppercased)                   # unpack to print all

# With *args (accept any number of positional arguments)
def yell(*words):                    # *words collects all args into a tuple
    print(*map(str.upper, words))

yell("This", "is", "CS50")         # → THIS IS CS50
```

---

## 4. Generators (`generators.py`)

### Concept

A **generator** uses `yield` instead of `return`. It produces values **one at a time** (on demand), which is memory-efficient for large or infinite sequences. Contrast with a function that builds and returns an entire list.

- `return` → function ends, returns one value.
- `yield` → function pauses, hands back one value, resumes from the same spot next call.

### Code

```python
# Regular function — builds the whole list in memory
def sheep(n):
    flock = []
    for i in range(1, n + 1):
        flock.append("|Sheep|" * i)
    return flock          # if n = 1,000,000 this fills RAM

# Generator — produces values lazily
def sheep(n):
    for i in range(1, n + 1):
        yield "|Sheep|" * i   # produces one value, then pauses

# Usage is identical
for s in sheep(5):
    print(s)
# |Sheep|
# |Sheep||Sheep|
# |Sheep||Sheep||Sheep|
# ...
```

> **Rule of thumb**: if you only need to loop through the results once and there could be many, use a generator. If you need to access elements by index, use a list.

---

## 5. Unpacking (`unpacking.py`)

### Concept

Python lets you "unpack" a list or dict into individual variables or function arguments.

- `*` unpacks a list/tuple into positional arguments.
- `**` unpacks a dict into keyword arguments.
- `*args` in a function signature collects extra positional args into a tuple.
- `**kwargs` collects extra keyword args into a dict.

### Code

```python
# Unpack into variables
first, last = input("Full name? ").split(" ")
print(f"Hello, {first}")

# ---

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

# Pass list elements as positional args using *
coins = [100, 50, 25]
print(total(*coins))     # same as total(100, 50, 25)

# Pass dict as keyword args using **
coins = {"galleons": 100, "sickles": 50, "knuts": 25}
print(total(**coins))    # same as total(galleons=100, sickles=50, knuts=25)

# ---

# *args in definition: collect all positional args
def f(*args, **kwargs):
    print("Positional:", args)    # tuple
    print("Named:", kwargs)       # dict

f(100, 50, 25, galleons=50)
# Positional: (100, 50, 25)
# Named: {'galleons': 50}
```

---

## 6. Sets (`set_datatype.py`)

### Concept

A **set** is an **unordered** collection of **unique** items. Automatically removes duplicates. Fast for membership checks (`in`). Created with `set()` or `{a, b, c}`.

### Code

```python
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry",    "house": "Gryffindor"},
    {"name": "Ron",      "house": "Gryffindor"},
    {"name": "Draco",    "house": "Slytherin"},
    {"name": "Padma",    "house": "Ravenclaw"},
]

# List approach: must manually check duplicates
houses = []
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])    # O(n) per check

# Set approach: unique by nature, O(1) membership check
houses = set()
for student in students:
    houses.add(student["house"])           # duplicates ignored automatically

for house in sorted(houses):
    print(house)
# Gryffindor
# Ravenclaw
# Slytherin

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)   # union:        {1, 2, 3, 4, 5}
print(a & b)   # intersection: {3}
print(a - b)   # difference:   {1, 2}
```

---

## 7. Global Variables vs. Classes (`global_variable.py`)

### Concept

The `global` keyword lets a function modify a variable defined at the module level. **Avoid this pattern** — it makes code hard to debug. The right fix is using a class.

### Code

```python
# BAD: global variable approach
balance = 0

def deposit(n):
    global balance       # without this, Python assumes local variable
    balance += n

def withdraw(n):
    global balance
    balance -= n

deposit(100)
withdraw(50)
print(balance)   # 50

# ---

# BETTER: encapsulate state in a class
class Account:
    def __init__(self):
        self._balance = 0    # private by convention

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n   # self replaces global — no global needed

    def withdraw(self, n):
        self._balance -= n

account = Account()
account.deposit(100)
account.withdraw(50)
print(account.balance)   # 50
```

---

## 8. Type Hints (`type_hint.py`)

```python
# Syntax: param: type, return -> type
def greet(name: str) -> str:
    return f"Hello, {name}"

def add(a: int, b: int) -> int:
    return a + b

def process(items: list[str]) -> None:
    for item in items:
        print(item)
```

> Type hints are **not enforced** at runtime — they're documentation for humans and tools like `mypy`.

---

## 9. Docstrings (`doc_strings.py`)

```python
def square(n: int) -> int:
    """
    Return the square of n.

    Args:
        n (int): The number to square.

    Returns:
        int: The square of n.
    
    Example:
        >>> square(4)
        16
    """
    return n * n

# Access via help() or .__doc__
help(square)
print(square.__doc__)
```

---

# MODULE 4 — NewPython (OOP)

## The Big Picture

OOP organizes code around **objects** — things that have:
- **Attributes** (data / state): name, house, balance
- **Methods** (behavior / actions): speak, sort, deposit

A **class** is the blueprint; an **object** (instance) is what you build from it.

---

## OOP1: Classes, `__init__`, `__str__`, Properties

### Step-by-step evolution toward a full class

**Step 1 — Just functions with separate variables (too loose)**
```python
name = input("Name: ")
house = input("House: ")
print(f"{name} from {house}")
```

**Step 2 — Tuple (can't change values, no labels)**
```python
# Tuples use ()  — immutable; lists use [] — mutable
student = ("Harry", "Gryffindor")
print(student[0])    # positional — unclear what [0] means
```

**Step 3 — Dict (labeled, mutable, but no validation)**
```python
student = {"name": "Harry", "house": "Gryffindor"}
print(student["name"])
```

**Step 4 — Class (labeled, mutable, validation, behavior)**
```python
class Student:
    def __init__(self, name, house):
        # __init__ = constructor. Called automatically when you do Student(...)
        # self = the specific instance being created
        self.name = name
        self.house = house

    def __str__(self):
        # Called automatically by print(student) or str(student)
        return f"{self.name} from {self.house}"

student = Student("Harry", "Gryffindor")
print(student)         # triggers __str__ → "Harry from Gryffindor"
print(student.name)    # attribute access
```

### Validation in `__init__`

```python
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
```

### Instance Methods

Methods are just functions inside a class that take `self` as first arg.

```python
class Student:
    def __init__(self, name, house, patronus):
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":         return ":)"
            case "Otter":        return ";)"
            case "Jack Russell": return ":>"
            case _:              return ":/"

s = Student("Harry", "Gryffindor", "Stag")
print(s.charm())    # → :)
```

### Properties: Getters & Setters

**Why?** You want to validate every time an attribute is set — even after construction.

```python
class Student:
    def __init__(self, name, house):
        self.name = name       # ← goes through @name.setter
        self.house = house     # ← goes through @house.setter

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):             # GETTER — called when you READ self.name
        return self._name

    @name.setter
    def name(self, name):       # SETTER — called when you WRITE self.name = ...
        if not name:
            raise ValueError("Missing name")
        self._name = name       # store in _name (private by convention)

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
```

> **Naming convention**: `_var` = "private by convention" (Python doesn't truly enforce it). `__var` = name-mangled (harder to access externally).

---

## OOP2: Class Variables & Class Methods

| Feature | Instance Variable | Class Variable |
|---------|-----------------|----------------|
| Defined in | `__init__` with `self.` | Directly in the class body |
| Belongs to | Each **instance** | The **class** itself (shared) |
| Accessed via | `self.attr` | `cls.attr` or `ClassName.attr` |

```python
import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    # ↑ class variable: shared across all Hat instances

    @classmethod
    def sort(cls, name):        # cls = the class itself (not an instance)
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry")   # called on the class directly — no instance needed
```

**Factory class method** — alternative constructor:

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):               # factory: handles input and creates instance
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house) # cls(...) = Student(...)

def main():
    student = Student.get()    # call factory directly on class
    print(student)

if __name__ == "__main__":
    main()
```

---

## OOP3: Inheritance (`OOP3.py`)

### Concept

**Inheritance** lets a child class reuse and extend the code from a parent class.
- `class Child(Parent)` — Child inherits everything from Parent.
- `super().__init__(...)` — calls Parent's `__init__` to set shared attributes.
- Child can override parent methods (polymorphism).

```python
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name
    ...

class Student(Wizard):           # Student IS-A Wizard
    def __init__(self, name, house):
        super().__init__(name)   # delegate name validation to Wizard
        self.house = house       # add Student-specific attribute

    def __str__(self):
        return f"{self.name} from {self.house}"
    ...

class Professor(Wizard):         # Professor IS-A Wizard too
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    ...

# All three work independently
wizard    = Wizard("Albus")
student   = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")
```

> **IS-A vs HAS-A**: Prefer inheritance for "IS-A" relationships. Use a separate object (composition) for "HAS-A".

---

## OOP4: Operator Overloading & Exception Hierarchy (`OOP4.py`)

### Operator Overloading

Python lets you define what `+`, `-`, `*`, `==`, `<`, etc. mean for your custom class, by defining **dunder methods**.

```python
class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles  = sickles
        self.knuts    = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other):      # enables: vault1 + vault2
        return Vault(
            self.galleons + other.galleons,
            self.sickles  + other.sickles,
            self.knuts    + other.knuts
        )

potter  = Vault(100, 50, 25)
weasley = Vault(25, 50, 100)
total   = potter + weasley         # calls __add__
print(total)                       # → 125 Galleons, 100 Sickles, 125 Knuts
```

**Common dunder methods**:

| Dunder | Operator / Usage |
|--------|-----------------|
| `__init__` | `ClassName()` construction |
| `__str__` | `print(obj)`, `str(obj)` |
| `__repr__` | Developer-facing representation |
| `__add__` | `obj1 + obj2` |
| `__sub__` | `obj1 - obj2` |
| `__mul__` | `obj1 * obj2` |
| `__eq__` | `obj1 == obj2` |
| `__lt__` | `obj1 < obj2` |
| `__len__` | `len(obj)` |
| `__getitem__` | `obj[key]` |

### Python Exception Hierarchy

```
BaseException
 ├── KeyboardInterrupt        ← Ctrl+C
 └── Exception
      ├── ArithmeticError
      │    └── ZeroDivisionError
      ├── AssertionError
      ├── AttributeError       ← obj has no such attribute
      ├── EOFError
      ├── ImportError
      │    └── ModuleNotFoundError
      ├── LookupError
      │    ├── KeyError         ← dict key not found
      │    └── IndexError       ← list index out of range
      ├── NameError            ← variable not defined
      ├── OSError
      │    └── FileNotFoundError
      ├── SyntaxError
      │    └── IndentationError
      ├── TypeError            ← wrong type passed
      └── ValueError           ← right type, wrong value
```

---

# 🔑 Master Cheatsheet

## Data Types

| Type | Example | Mutable? | Ordered? | Unique? |
|------|---------|----------|----------|---------|
| `str` | `"hello"` | ✗ | ✓ | ✗ |
| `int` | `42` | ✗ | — | — |
| `float` | `3.14` | ✗ | — | — |
| `list` | `[1,2,3]` | ✓ | ✓ | ✗ |
| `tuple` | `(1,2,3)` | ✗ | ✓ | ✗ |
| `dict` | `{"a":1}` | ✓ | ✓ (3.7+) | keys ✓ |
| `set` | `{1,2,3}` | ✓ | ✗ | ✓ |

## Comprehension Patterns

```python
# List
[expr for item in iterable]
[expr for item in iterable if condition]

# Dict
{key: val for item in iterable}

# Set
{expr for item in iterable}

# Generator (lazy — use inside functions)
(expr for item in iterable)
```

## OOP Quick Reference

```
Class Blueprint:
  __init__(self, ...)  → constructor
  __str__(self)        → string representation
  @property            → getter
  @attr.setter         → setter (validates writes)
  @classmethod         → belongs to class, not instance (cls)
  @staticmethod        → no self or cls needed

Object creation:
  obj = MyClass(args)  → calls __init__
  print(obj)           → calls __str__
  obj.attr             → getter
  obj.attr = val       → setter
```

## Running Code

```bash
# Run any file
python3 "Start_Python/3. function.py"

# Run with CLI argument
python3 "Start_Python/17. APIS.py" taylor

# Run tests
cd BasicPythonStructures && pytest test_cal.py -v

# Run argparse tool
python3 ExtraPython/arg_parse.py -n 5
```

---

*Personal Python reference — Kalpit Rathod*
