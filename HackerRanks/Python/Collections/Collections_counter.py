from collections import Counter
import sys

line = sys.stdin.readlines()

num_shoes = int(line[0].strip())
size_shoes = line[1].strip().split(' ')
num_customer = int(line[2].strip())
corr_value = line[3:]
total_money = 0

count_shoes = Counter(size_shoes)
for element in corr_value:
    size = element.rstrip().split(' ')[0]
    money = element.rstrip().split(' ')[1]
    if size in size_shoes:
        if count_shoes[size] > 0:
            count_shoes[size] = count_shoes[size] - 1
            total_money += int(money)
        else:
            continue
    else:
        continue
sys.stdout.write(str(total_money))