import math
import os
import random
import re
import sys

"""
list a have to need to get lcm(least common multiply).
"""

def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

def multi_gcd(b):
    init_b = b[0]
    for i in range(len(b)):
        init_b = gcd(init_b, y=b[i])
    return init_b

def lcm(a):
    result = 0
    init_a = a[0]
    for num in range(len(a)):
        result = init_a * a[num] // multi_gcd([init_a, a[num]])
    return result

def getTotalX(a, b):
    # Write your code here
    result = []
    gcd_value = multi_gcd(b)
    lcm_value = lcm(a)
    int_num = int(gcd_value / lcm_value)
    for num in range(1, int_num+1):
        boolean = []
        for ele in a+b:
            if (lcm_value * num) >= ele:
                if (lcm_value * num) % ele == 0: boolean.append(True)
            else:
                if ele % (lcm_value * num) == 0: boolean.append(True)
        if len(boolean) == len(a+b): result.append(lcm_value*num)

    return len(result)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])

    # m = int(first_multiple_input[1])

    # arr = list(map(int, input().rstrip().split()))

    # brr = list(map(int, input().rstrip().split()))

    # total = getTotalX(arr, brr)
    # total = getTotalX([2, 6], [24, 36])
    # total = getTotalX([2, 4], [16, 32, 96])
    total = getTotalX([4], [16])
    print(total)
    # total = getTotalX([3, 4], [24, 48])
    # fptr.write(str(total) + '\n')

    # fptr.close()
