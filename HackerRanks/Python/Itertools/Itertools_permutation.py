from itertools import permutations
import sys

def method_v1():
    for S in sys.stdin:
        string, value = S.split()[0], int(S.split()[1])
        permu_s = list(permutations(sorted(string), value))

        for str_tuple in permu_s:
            answer = ''.join(str_tuple)
            sys.stdout.write(answer + '\n')

def method_v2():
    line = sys.stdin.readline().strip()
    string = sorted(line.split(' ')[0])
    integer = int(line.split(' ')[1])

    permu = permutations(string, integer)
    for ans in permu:
        ans_str = ''.join(ans)
        print(ans_str)