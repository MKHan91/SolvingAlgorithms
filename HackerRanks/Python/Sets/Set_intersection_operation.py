import sys

line = sys.stdin.readlines()

n = int(line[0].strip())
n_roll_num = set(line[1].strip().split(' '))
b = int(line[2].strip())
b_roll_num = set(line[3].strip().split(' '))

ans = len(n_roll_num.intersection(b_roll_num))
sys.stdout.write(str(ans))