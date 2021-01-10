#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max_value_list = []
    min_value_list = []
    max_value = min_value = scores[0]
    for ele in scores[1:]:
        if ele > max_value:
            max_value = ele
            max_value_list.append(max_value)
        elif ele < min_value:
            min_value = ele
            min_value_list.append(min_value)
    
    return len(max_value_list), len(min_value_list)

def breakingRecords_v2(scores):
    idx_max_value = 0
    idx_min_value = 0
    max_value = min_value = scores[0]
    for ele in scores[1:]:
        if ele > max_value:
            max_value = ele
            idx_max_value += 1
        elif ele < min_value:
            min_value = ele
            idx_min_value += 1
    
    return idx_max_value, idx_min_value

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())max_value += 1

    # scores = list(map(int, input().rstrip().split()))

    # result = breakingRecords(scores)
    result = breakingRecords_v2([10, 5, 20, 20, 4, 5, 2, 25, 1])

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
