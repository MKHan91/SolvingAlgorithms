import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def find_prime_number(prime_numbers, number=0):
    for integer in range(3, 101):
        for number in range(2, 101):
            if integer != number:
                # print('integer:{}, number:{}'.format(integer, number))
                if integer % number != 0:
                    continue
                else:
                    break
        if integer % number == 0:
            continue
        prime_numbers.append(integer)
    return prime_numbers

def check_prime_number(numbers, prime_numbers):
    result = []
    for number in numbers:
        if number in prime_numbers:
            result.append('PRIME')
    if len(result) == len(numbers):
        return 1
    else:
        return 0
    
def getTotalX(a, b):
    # Write your code here
    result = []
    factorization = []
    init_numbers = [2]
    prime_numbers = find_prime_number(init_numbers)
    check_value_a = check_prime_number(a, prime_numbers)
    if check_value_a == 1:
        factor = math.prod(a)
    else:
        for num_a in a:
            # factorization += [int(num_a/prime_num)for prime_num in prime_numbers if num_a % prime_num == 0]
            for prime_num in prime_numbers:
                if num_a % prime_num == 0:
                    factorization.append(int(num_a/prime_num))
                    break
            continue
        factorization += [prime_num]
        factor = math.prod(factorization)

    check = []
    idx = 0
    for idx in range(1, len(a+b)):
        for num_ab, ele in enumerate(a+b):
            if ele <= (factor*idx):
                if (factor*idx) % ele == 0:
                    check.append('YES')
                else:
                    break
            else:
                if ele % (factor*idx) == 0:
                    check.append('YES')
                else:
                    break
            if num_ab + 1 == len(a+b): break
        if num_ab + 1 != len(a+b): continue
    return len([factor*num_idx for num_idx in range(1, idx)])

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])

    # m = int(first_multiple_input[1])

    # arr = list(map(int, input().rstrip().split()))

    # brr = list(map(int, input().rstrip().split()))

    # total = getTotalX(arr, brr)
    # total = getTotalX([2, 4], [16, 32, 96])
    total = getTotalX([2, 3, 4], [24, 36])
    print(total)
    a=1
    # fptr.write(str(total) + '\n')

    # fptr.close()
