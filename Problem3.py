#Problem Statement  link ==>https://www.hackerrank.com/challenges/migratory-birds/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    lst2 = []
    for i in range(1,6):
        lst2.append(arr.count(i))

    result = max(lst2)


    return lst2.index(result) +1

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
