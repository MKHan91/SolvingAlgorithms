import sys

line = sys.stdin.readlines()
total_num = int(line[0].strip())
conuntry = line[1:]
ans = []
for c in conuntry:
    ans.append(c.strip())
sys.stdout.write(str(len(set(ans))))