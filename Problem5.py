#problem ==>  https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    a1 = abs(z-x)
    a2 = abs(z-y)
    if(a1 == a2):
        return "Mouse C"

    if(a1 > a2):
        return "Cat B"
    else:
        return "Cat A"        



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
