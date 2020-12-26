#!/bin/python3
import math
import os
import random
import re
import sys

def solution():
    N, M = map(int, input().split())
    rows = [input() for _ in range(N)]
    k = int(input())

    for row in sorted(rows, key=lambda row : int(row.split()[k])):
        print(row)

def my_solution():
    nm = input().split(' ')

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    print(arr)
    sorting = [sorted(ele) for num, ele in enumerate(zip(*arr)) if num == k][0]
    for sorting_ele in sorting:
        for idx, eles in enumerate(arr):
            if sorting_ele == eles[k]:
                print(eles)
                del arr[idx]
                string_eles = [str(ele) for ele in eles]
                print(" ".join(string_eles))

if __name__ == '__main__':
    solution()