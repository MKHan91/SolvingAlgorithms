def solution(n):
    f0, f1 = 0, 1
    if n == 2:
        answer = f0 + f1
    else:
        answer = 1 + solution(n-1)
    return answer

if __name__ == "__main__":
    n = 4
    print(solution(n))