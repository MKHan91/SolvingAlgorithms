import sys

line = sys.stdin.readlines()

n = int(line[0].strip())
n_roll_num = line[1].strip().split(' ')

b = int(line[2].strip())
b_roll_num = line[3].strip().split(' ')

n_set = set(n_roll_num)
b_set = set(b_roll_num)
ans = str(len(n_set.union(b_set)))
sys.stdout.write(ans)