set_A = set(input().split(' '))
N = int(input())

other_sets = list(set(input().split(' ')) for _ in range(N))

ans_list = [set_A.issuperset(set_ele) for set_ele in other_sets]
ans = 1
for element in ans_list:
    ans *= element
if ans == 1:
    print('True')
elif ans == 0:
    print('False')