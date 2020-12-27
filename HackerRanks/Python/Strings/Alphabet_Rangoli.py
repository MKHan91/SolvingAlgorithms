import string

def print_rangoli(size):
    alpha = string.ascii_lowercase
    L = []
    for i in range(size):
        _str = '-'.join(alpha[i:size])
        L.append((_str[::-1] + _str[1:]).center(4*size-3, '-'))
    print('\n'.join(L[:0:-1] + L))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)