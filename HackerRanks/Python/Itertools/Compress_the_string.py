import sys
from itertools import groupby

def method_v1():
    Input = sys.stdin

    for sample in Input:
        sample = sample.rstrip('\n')
        samples = list(sample)
        if len(set(samples)) == 1:
            sys.stdout.write(str((len(samples), int(samples[0]))) + ' ')

        for num in range(len(samples)):
            for cnt in range(len(samples)):
                try:
                    samples[num] == samples[num+cnt]
                except IndexError:
                    if num == len(samples)-1:
                        if samples[num - 1] == samples[num]:
                            break
                    sys.stdout.write(str((cnt, int(samples[num])))+' ')
                    break
                if num > 0 and samples[num - 1] == samples[num]:
                    break
                elif samples[num] != samples[num+cnt]:
                    sys.stdout.write(str((cnt, int(samples[num])))+' ')
                    break
        break

def method_v2():
    line = sys.stdin.readline().rstrip()
    for _, value in groupby(line):
        ans = list(value)
        sys.stdout.write('(' + str(len(ans)) + ', ' + ans[0] + ')' + ' ')