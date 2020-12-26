from collections import defaultdict
import sys

lines = sys.stdin.readlines()
n = int(lines[0].split(' ')[0].strip())
m = int(lines[0].split(' ')[1].strip())

words = lines[1:]
d = defaultdict(list)
for num in range(len(words)):
    if num <= n-1:
        d['group_A'].append(words[num].strip())
    else:
        d['group_B'].append(words[num].strip())

for value in d['group_B']:
    if value in d['group_A']:
        ans = [str(index+1) for index, x in enumerate(d['group_A']) if x == value]
        sys.stdout.write(' '.join(ans) + '\n')
    else:
        sys.stdout.write(str(-1) + '\n')
