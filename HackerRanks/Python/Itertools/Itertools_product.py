# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
import sys

A = sys.stdin.readline().rstrip().split(' ')
B = sys.stdin.readline().rstrip().split(' ')

for char_tup in product(A, B):
    sys.stdout.write('('+', '.join(char_tup)+')'+' ')