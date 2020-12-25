import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sort_arr = sorted(arr)
    min = sum(sort_arr[:4])
    max = sum(sort_arr[::-1][:4])
    print(min, max)
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
