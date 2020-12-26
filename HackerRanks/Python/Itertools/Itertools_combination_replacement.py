from itertools import combinations_with_replacement
import sys

def method_v1():
    Input = sys.stdin
    for sample in Input:
        string, value = sample.split()[0], int(sample.split()[1])
        combin_repl = sorted(list(combinations_with_replacement(string, value)))

        new_sample_list = []
        for sort_sample in combin_repl:
            new_sample_list += [sorted(sort_sample)]

        for answer in sorted(new_sample_list):
            sys.stdout.write(''.join(answer) + '\n')
        break


def method_v2():
    line = sys.stdin.readline().strip()
    string = sorted(line.split(' ')[0])
    integer = int(line.split(' ')[1])

    list_combin_rep = list(combinations_with_replacement(string, integer))
    for ans in list_combin_rep:
        ans = ''.join(ans)
        sys.stdout.write(ans+'\n')