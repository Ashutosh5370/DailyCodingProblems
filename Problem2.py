#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    totalbill = sum(bill)

    anna = int((totalbill - bill[k])/ 2)


    if(anna == b):
        print("Bon Appetit")

    else:
        print(b - anna)    






if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)


Anna and Brian are sharing a meal at a restuarant and they agree to split the bill equally. Brian wants to order something that Anna is allergic to though, and they agree that Anna won't pay for that item. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.

For example, assume the bill bill = [2,4,6] has the following prices: . Anna declines to eat item  which costs k = bill[2]. If Brian calculates the bill correctly, Anna will pay (2+4)/2. If he includes the cost of b[2] , he will calculate (2+4 +6)/2. In the second case, he should refund  to Anna. 3

