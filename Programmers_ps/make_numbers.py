def solution(x, n):
    if x < 0:
        answer = list(range(x, x*n-1, x))
    elif x > 0:
        answer = list(range(x, x*n+1, x))
    elif x == 0:
        answer = [0] * n
    return answer

def solution2(x, n):
    return [i * x + x for i in range(n)]

if __name__ == "__main__":
    x, n = 2, 5
    print(solution(x, n))