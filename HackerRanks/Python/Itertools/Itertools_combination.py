from itertools import combinations
import sys

def method_v1():
    Input = sys.stdin

    for sample in Input:
        string, value = sample.split()[0], int(sample.split()[1])
        for num in range(1, value+1):
            new_answer_list = []
            combin = sorted(list(combinations(string, num)))

            for answer in combin:
                answer_lower = sorted(answer, key=str.lower)
                new_answer_list += [answer_lower]
            for answer_v2 in sorted(new_answer_list):
                sys.stdout.write(''.join(answer_v2) + '\n')
        break

def method_v2():
    line = sys.stdin.readline()
    string = sorted(line.split(' ')[0])
    integer = int(line.split(' ')[1])

    for num in range(1, integer + 1):
        list_combin = list(combinations(string, num))
        for ans in list_combin:
            print(''.join(ans))