def print_formatted(number):
    width = len(format(number, 'b'))
    for decimal in range(1, number+1):
        print(str(decimal).rjust(width) + str(format(decimal, 'o')).rjust(width+1) + str(format(decimal, 'X')).rjust(width+1) + str(format(decimal, 'b')).rjust(width+1))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)