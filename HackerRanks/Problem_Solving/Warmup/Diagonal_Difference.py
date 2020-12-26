#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    first_sum = []
    second_sum = []
    for i in range(len(arr)):
        first_sum.append(arr[i][i])
    for j in range(len(arr)):
        second_sum.append(arr[j][len(arr)-j-1])

    return abs(sum(first_sum) - sum(second_sum))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
