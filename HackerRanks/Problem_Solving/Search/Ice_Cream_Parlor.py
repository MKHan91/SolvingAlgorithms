import math
import os
import random
import re
import sys

def icecreamParlor(m, arr):
    # Write your code here
    result = []
    for num in range(len(arr)):
        for step in range(len(arr)-(num+1)):
            if arr[num] + arr[step+(num+1)] == m:
                result.append([num+1, step+(num+1)+1])
    result = sorted(result[0])
    return result

if __name__ == '__main__':
    m = 9 # 돈
    n = 5 # cost 배열의 길이
    arr = [1, 3, 4, 6, 7, 9]
    result = icecreamParlor(m, arr)
    print(result)
