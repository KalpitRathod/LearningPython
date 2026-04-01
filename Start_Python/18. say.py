import sys

from printlib import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])