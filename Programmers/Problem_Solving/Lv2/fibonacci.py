def solution(n):
    # 재귀 함수를 쓸 경우 iterative 방법보다 더 많은 시간 복잡도 소요
    if n <= 1:
        answer = n
    else:
        answer = solution(n-2) + solution(n-1)
        answer %= 1234567
    return answer

def iterative_solution(n):
    fibonacci_series = [0, 1]
    if n <= 1:
        answer = n
    else:
        for i in range(1, n):
            value = fibonacci_series[i-1] + fibonacci_series[i]
            fibonacci_series.append(value)
    answer = fibonacci_series[-1] % 1234567
    return answer

if __name__ == "__main__":
    n = 4
    # print(solution(n))
    print(iterative_solution(n))