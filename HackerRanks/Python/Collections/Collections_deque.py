from collections import deque

d = deque()

def method_v2():
    strings = [input().split(' ') for _ in range(int(input()))]
    for string in strings:
        if string[0] == 'append':
            d.append(string[1])
        elif string[0] == 'pop':
            d.pop()
        elif string[0] == 'popleft':
            d.popleft()
        elif string[0] == 'appendleft':
            d.appendleft(string[1])

def method_v1():
    command, value = 0, 0
    for _ in range(int(input())):
        string = input().split(' ')
        if len(string) == 2:
            command, value = string[0], int(string[1])
        else:
            command = string[0]

        if command == 'append':
            d.append(value)
        elif command == 'pop':
            d.pop()
        elif command == 'popleft':
            d.popleft()
        elif command == 'appendleft':
            d.appendleft(value)

    print(' '.join(str(x) for x in list(d)))