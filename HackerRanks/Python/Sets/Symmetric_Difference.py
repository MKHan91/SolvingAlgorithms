import sys

line = sys.stdin.readlines()

M = map(int, line[0].strip())
N = map(int, line[2].strip())

M_set = set(line[1].strip().split(' '))
N_set = set(line[3].strip().split(' '))

ans = map(int, M_set.symmetric_difference(N_set))
for ans_element in sorted(ans):
    sys.stdout.write(str(ans_element))
    sys.stdout.write('\n')