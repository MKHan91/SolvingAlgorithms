import sys

line = sys.stdin.readlines()

eng_num_stu = map(int, line[0].strip())
fre_num_stu = map(int, line[2].strip())

eng_rollnum = set(line[1].strip().split(' '))
fre_rollnum = set(line[3].strip().split(' '))

ans = eng_rollnum.symmetric_difference(fre_rollnum)
sys.stdout.write(str(ans))