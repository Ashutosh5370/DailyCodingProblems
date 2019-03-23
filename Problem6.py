
#Problem link = >https://www.hackerrank.com/challenges/designer-pdf-viewer/problem


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):

    lst = []
    for c in word:
        lst.append(ord(c))

    lst2 = []

    for i in lst:
        lst2.append(i-97)

    #print(lst2)

    max = 0

    for j in lst2:
        if(h[j]>max):
            max = h[j]

    #print(max)        

    result = max * len(lst2)

    #print(result)
    return result








if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
