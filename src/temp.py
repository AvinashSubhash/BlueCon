import sys
import time
import select
import os

for i in range(10):
    os.system('clear')
    sys.stdout.write("\r{0}".format(i))
    sys.stdout.flush()
    i, o, e = select.select( [sys.stdin], [], [], 4 )
    if i and sys.stdin.readline().strip()=="-1":
        exit(0)
