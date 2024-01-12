'''
import sys #argv will be usable when user hit enter before typing something

# print(sys.argv[0]) #this is name of the file
print("hello, my name is", sys.argv[1]) # this will generate index error if you dont give the aeguments while running in the commandline
'''

'''
import sys

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
'''

'''
import sys

if len(sys.argv) < 2:
    print("Too few argument")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])
'''

'''
import sys

# Check for errors
if len(sys.argv) < 2:
    sys.exit("Too few argument")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

# Print name tags
print("hello, my name is", sys.argv[1])
'''

'''
import sys

if len(sys.argv) < 2:
    sys.exit("Too few argument")

for name in sys.argv[1: ]:
    print("hello, my name is", name)
'''