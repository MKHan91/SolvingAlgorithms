import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for leng in range(n):
        print(('#'*(leng+1)).rjust(n))
        
if __name__ == '__main__':
    n = int(input())

    staircase(n)
