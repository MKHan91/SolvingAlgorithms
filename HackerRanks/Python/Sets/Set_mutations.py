import sys

line = sys.stdin.readlines()

num_A = int(line[0].strip())
A = set(line[1].strip().split(' '))
N = int(line[2].strip())

for idx in range(1, N+1):
    op_name = line[2*idx+1].strip().split(' ')[0]
    other_set = set(line[2*idx+2].strip().split(' '))

    if op_name == 'update':
        A.update(other_set)
    elif op_name == 'intersection_update':
        A.intersection_update(other_set)
    elif op_name == 'difference_update':
        A.difference_update(other_set)
    elif op_name == 'symmetric_difference_update':
        A.symmetric_difference_update(other_set)

ans = sum(list(map(int, A)))
sys.stdout.write(str(ans))