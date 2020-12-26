from itertools import product
import sys

def method_v1():
    line = sys.stdin.readlines()
    K, M =int((line[0].strip()).split(' ')[0]), int((line[0].strip()).split(' ')[1])

    int_N = []
    for num in range(K):
        str_N = (line[num+1].strip()).split(' ')
        int_N.append(list(map(int, str_N)))

    total_sum = map(lambda x: sum(element**2 for element in x) % M, product(*int_N))
    sys.stdout.write(str(max(total_sum)))


def method_v2():
    K,M = map(int,input().split())
    N = (list(map(int, input().split()))[1:] for _ in range(K))
    results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
    print(max(results))