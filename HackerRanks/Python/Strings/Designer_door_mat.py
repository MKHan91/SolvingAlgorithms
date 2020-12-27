import sys

char = 'WELCOME'
L_char = len(char)

line = sys.stdin.readline()
N = int(line.split()[0])
M = int(line.split()[1])
for length in range(1, (N-1)//2+2):
    if length <= (N-1)/2:
        sys.stdout.write(('-'*((M-(6*length-3))//2)).rjust((M-(6*length-3))//2) + ('.|.'*((2*length-1))).center(6*length-3) + ('-'*((M-(6*length-3))//2)).ljust((M-(6*length-3))//2))
        sys.stdout.write('\n')
    elif length == (N-1)/2+1:
        sys.stdout.write(('-'*((M-L_char)//2)).rjust((M-L_char)//2) + char.center(L_char) + ('-'*((M-L_char)//2)).ljust((M-L_char)//2))
        sys.stdout.write('\n')
for length in reversed(range(1, (N-1)//2+1)):
    sys.stdout.write(('-'*((M-(6*length-3))//2)).rjust((M-(6*length-3))//2) + ('.|.'*((2*length-1))).center(6*length-3) + ('-'*((M-(6*length-3))//2)).ljust((M-(6*length-3))//2))
    sys.stdout.write('\n')
