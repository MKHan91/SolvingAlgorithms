import sys

line = sys.stdin.readlines()
first_line = list(map(int, line[0].strip().split(' ')))

n, m = first_line[0], first_line[1]
array = line[1].strip().split(' ')
A = set(line[2].strip().split(' '))
B = set(line[3].strip().split(' '))

score = 0
for element in array:
    if element in A:
        score += 1
    elif element in B:
        score -= 1

sys.stdout.write(str(score))