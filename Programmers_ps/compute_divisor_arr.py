def solution(arr, divisor):
    answer = []
    arr = sorted(arr)
    while len(arr) > 0:
        if arr[-1] % divisor == 0:
            answer.append(arr[-1])
            arr.pop(-1)
        else:
            arr.pop(-1)
    answer = sorted(answer)
    if len(answer) == 0:
        answer = [-1]
    return answer

def solution2(arr, divisor):
    answer = sorted([ele for ele in arr if ele % divisor == 0]) or [-1]
    return answer

if __name__ == "__main__":
    arr = [50, 5, 65, 8, 22, 0]
    divisor = 10
    print(solution2(arr, divisor))