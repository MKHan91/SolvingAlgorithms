import re

num_test_cases = int(input())
for _ in range(num_test_cases):
    input_ = input()
    try:
        re.compile(input_)
        print("True")
    except re.error:
        print("False")