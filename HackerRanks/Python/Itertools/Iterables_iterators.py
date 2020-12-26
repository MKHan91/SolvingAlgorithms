import sys
from itertools import combinations

line = sys.stdin.readlines()
N = int(line[0].strip())
string = line[1].strip().split(' ')
K = int(line[2].strip())

str_list = list(combinations(string, K))
denominator = len(str_list)

for ans in str_list[:]:
    # print(ans, str_list)
    if not 'a' in ans:
        str_list.remove(ans)

sys.stdout.write(str(round(len(str_list)/denominator, 4)))