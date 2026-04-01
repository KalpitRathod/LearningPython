'''
email = input("what's your email? ").strip()

# if "@" and "." in email:
#     print("Valid")
# else:
#     print("Invalid")

username, domain = email.split("@")

# if (username) and ("." in domain):
if (username) and (domain.endswith(".edu")):
    print("Valid")
else:
    print("Invalid")
'''

'''
import re
# using re library re.search(pattern, string, flags=0)
# "." any character except a newline
# "*" 0 or more repetitions
# "+" 1 or more repetitions
# "?" 0 or 1 repetition
# "{m}" m repetitions
# "{m,n}" m-n repetitions
# "^" matches the start of the string
# "$" mathces the end of the string or just before the newline at the end of the string
# "[]" set of characters
# "[^]" complementing the set
# "\d" decimal digit
# "\D" not a decimal digit
# "\s" whitespace characters
# "\S" not a whitespace character
# "\w" word character ... as well as numbers and the underscore
# "\W" not a word character
# A|B either A or B
# (...) a group
# (?:...) non-capturing version
email = input("What's your email? ").strip()

# if re.search(r"^.+@.+\.edu$", email):
# if re.search(r"^[^@]+@[^@]+\.edu$", email): #Everything exept @ sign
# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
if re.search(r"^\w+@\w+\.(edu|com|gov|net)$", email):
    print("Valid")
else:
    print("Invalid")
'''

#Need to solve the dot problem that my username has the dot in between. and Uppercase and Lowercase problem that emails has only lowercase in it.
import re
# using re library re.search(pattern, string, flags=0)
# "." any character except a newline
# "*" 0 or more repetitions
# "+" 1 or more repetitions
# "?" 0 or 1 repetition
# "{m}" m repetitions
# "{m,n}" m-n repetitions
# "^" matches the start of the string
# "$" mathces the end of the string or just before the newline at the end of the string
# "[]" set of characters
# "[^]" complementing the set
# "\d" decimal digit
# "\D" not a decimal digit
# "\s" whitespace characters
# "\S" not a whitespace character
# "\w" word character ... as well as numbers and the underscore
# "\W" not a word character
# A|B either A or B
# (...) a group
# (?:...) non-capturing version
email = input("What's your email? ").strip()#.lower()
print(email)
# if re.search(r"^.+@.+\.edu$", email):
# if re.search(r"^[^@]+@[^@]+\.edu$", email): #Everything exept @ sign
# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
# some flags is re.IGNORECASE, re.MULTILINE, re.DOTALL
# re.match, re.fullmatch
if re.search(r"^(\w)+(\.)?@(\w+\.)?\w+\.(edu|com|gov|net)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")