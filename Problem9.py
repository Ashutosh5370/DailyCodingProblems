 Problem link = > https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
 
 #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.

def reversenu(Number):
    return int(str(Number)[::-1])



def beautifulDays(i, j, k):

    counter = 0 

    for x in range(i , j+1):

        reverse  = reversenu(x)

        print(reverse)

        result = abs(reverse - x ) / k

        print(result)

        if((result).is_integer()):
            counter += 1

    return counter        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
