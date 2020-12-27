#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    str_list = s.split(' ')
    for num in range(len(str_list)):
        if str_list[num] == '':
            continue
        elif str_list[num][0].islower():
            str_list[num] = str_list[num][0].upper() + str_list[num][1:]
        print(str_list[num])

    return ' '.join(str_list)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
