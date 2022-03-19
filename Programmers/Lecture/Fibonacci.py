def solution(x):
    if x <= 1:
        answer = x
    else:
        answer = solution(x-1) + solution(x-2)
    return answer

def iterative_solution(x):
    Fibonacci_series = [0, 1]
    if x <= 1:
        answer = x
    else:
        for i in range(1, x):
            value = Fibonacci_series[i-1] + Fibonacci_series[i]
            Fibonacci_series.append(value)
        
        answer = Fibonacci_series[-1]
    return answer
if __name__ == "__main__":
    x = 5
    # print(solution(x))
    print(iterative_solution(x))