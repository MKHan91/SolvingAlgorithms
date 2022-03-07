def solution(arr):
    idx = arr.index(min(arr))
    arr.pop(idx)
    if len(arr) == 0:
        answer = [-1]
    else:
        answer = arr
    return answer


if __name__ == "__main__":
    arr = [4,3,2,10]
    print(solution(arr))