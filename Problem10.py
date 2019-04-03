#problem link = > https://www.hackerrank.com/challenges/permutation-equation/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    n = len(p)
    print(n)
    lst= []
    for i in range(1,n+1):
        
        a = p.index(i)
        a = a+1
        b = p.index(a)
        b = b+1
        lst.append(b)

    

    return lst





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
