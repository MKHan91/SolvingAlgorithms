def solution(a, b):
    answer = 0
    if a > b:
        answer = sum([integer for integer in range(b, a+1)])
    elif a < b:
        answer = sum([integer for integer in range(a, b+1)])
    else:
        answer = a
    return answer

if __name__ == "__main__":
    a, b = 3, 5
    result = solution(a, b)
    print(result)