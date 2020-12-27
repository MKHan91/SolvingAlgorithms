import collections

if __name__ == '__main__':
    s = sorted(input().strip())
    "반복 횟수를 내림차순으로 정렬"
    s_counter = collections.Counter(s).most_common()
    "sorting 할 때 key 값을 기준으로 sorting"
    s_counter = sorted(s_counter, key=lambda x: (x[1] * -1, x[0]))
    print(s_counter)
    for i in range(3):
        print(s_counter[i][0], s_counter[i][1])
