#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    ans = []
    multiple_5 = [5*(num+1) for num in range(100)]
    for grad in grades:
        idx = [idx for idx, multiple in enumerate(multiple_5) if grad < multiple][0]
        if multiple_5[idx] < 40:
            ans.append(grad)
            continue
        elif abs(grad - multiple_5[idx]) < 3:
           ans.append(multiple_5[idx])
        elif abs(grad - multiple_5[idx]) >= 3:
            ans.append(grad)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
