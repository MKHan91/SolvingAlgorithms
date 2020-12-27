import sys

line = sys.stdin.readline()

N = int(line.strip())
for _ in range(N):
    len_A, A, len_B, B = sys.stdin.readline(), set(sys.stdin.readline().strip().split(' ')), sys.stdin.readline(), set(sys.stdin.readline().strip().split(' '))
    ans = A.issubset(B)
    sys.stdout.write(str(ans))
    sys.stdout.write('\n')