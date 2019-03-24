#problem Link =>https://www.hackerrank.com/challenges/utopian-tree/problem


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    lst = [x for x in range(n+1)]
    #print(lst)
    lst2 = []

    sum = 1 

    lst2.append(1)

    for i in lst[1:]:
        if(i%2 != 0):
            sum = sum*2
            lst2.append(sum)
            

        else:
            sum = sum + 1    
            lst2.append(sum)

    return lst2[-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
