def average(array):
    denominator = len(set(array))
    numerator = sum(set(array))
    avg = numerator / denominator

    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)