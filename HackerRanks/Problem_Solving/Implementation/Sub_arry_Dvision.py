#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    if m > 1:
        total_segments = []
        for idx in range(len(s)-1):
            for num in range(len(s[idx+1:])):
                segments = [s[idx]]
                segments += s[idx+num+1:][:m-1]
                if num != 0:
                    if segments in total_segments: continue
                total_segments.append(segments)
                print(total_segments)
                a=1
    else:
        a=1
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # s = list(map(int, input().rstrip().split()))

    # dm = input().rstrip().split()

    # d = int(dm[0])

    # m = int(dm[1])

    # result = birthday(s, d, m)
    result = birthday([1, 2, 1, 3, 2], 3, 2)

    # fptr.write(str(result) + '\n')

    # fptr.close()
