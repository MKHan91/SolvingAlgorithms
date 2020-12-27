n = int(input())
s = set(map(int, input().split()))

N = int(input())
ans = []
for num in range(N):
    str_value = input()
    string = str_value.split(' ')[0]

    if string == 'pop':
        ans.append(s.pop())
    elif string == 'remove':
        value = int(str_value.split(' ')[1])
        ans.append(s.remove(value))
    elif string == 'discard':
        value = int(str_value.split(' ')[1])
        ans.append(s.discard(value))

print(sum(s))