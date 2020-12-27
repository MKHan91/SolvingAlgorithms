import sys
from collections import Counter

line = sys.stdin.readlines()

K = int(line[0].strip())
room_num_list = sorted(line[1].strip().split(' '))
R = len(room_num_list) // K

cnt = Counter(room_num_list)
for key in cnt:
    if cnt[key] == 1:
        sys.stdout.write(key)