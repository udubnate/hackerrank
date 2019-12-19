#!/bin/python3

import math
import os
import random
import re
import sys

# if first character, then try to capitalize, if second or later then check previous character for space

# Complete the solve function below.
def solve(s):
    arr = list(s)
    lastchar = ''
    count = 0
    for c in arr:
        if lastchar == " " or count == 0:
            arr[count] = c.capitalize()
        lastchar = c
        count += 1
    return "".join(arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    print(result)
    fptr.write(result + '\n')

    fptr.close()
