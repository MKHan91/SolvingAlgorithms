if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    set_arr = list(set(arr))
    set_arr.remove(max(arr))

    print(max(set_arr))
    a=1