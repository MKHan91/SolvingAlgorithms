from collections import namedtuple
import sys

def method_v2():
    line = sys.stdin.readlines()
    N, column, ans = int(line[0].strip()), ' '.join(line[1].strip().split(' ')), 0
    spreadsheet = namedtuple('SpreadSheet', column)
    for idx in range(N):
        data = spreadsheet(' '.join(line[2+idx].strip().split(' ')))
        ans += int(data.MARKS)
    print(round(ans/N, 2))

def method_v1():
    N = int(input())

    column_line = input()
    list_column = [element for element in column_line.split(' ') if element]
    spreadsheet = namedtuple('SpreadSheet', ' '.join(list_column))
    ans = 0
    for _ in range(1, N+1):
        data_line = input()
        data_column = [data_element for data_element in data_line.split(' ') if data_element]
        spreadsheet_namdedtuple = spreadsheet(data_column[0], data_column[1], data_column[2], data_column[3])
        ans += int(spreadsheet_namdedtuple.MARKS)

    print(round(ans/N, 2))

def mehotd_v3():
    import collections, statistics
    print('%.2f' % statistics.mean(next(
        (int(student(*row).MARKS) for row in (input().split() for i in range(size))) for size, student in
        [[int(input()), collections.namedtuple('Student', input())]])))

if __name__ == '__main__':
    method_v2()