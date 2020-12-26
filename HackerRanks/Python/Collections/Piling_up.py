from collections import deque

T = int(input())
for _ in range(T):
    len_cubes, cubes = int(input()), deque(input().split(' '))
    for _ in range(len(cubes)-1):
        if cubes[0] >= cubes[-1]:
            cubes.popleft()
            if cubes[-1] < cubes[0]:
                print("No")
                break
            else:
                cubes.pop()
                if len(cubes) == 0:
                    print("Yes")
                    break
        else:
            print("No")
            break

