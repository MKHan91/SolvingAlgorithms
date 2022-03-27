def solution(n):
    answer = sorted([int(num) for num in str(n)], reverse=True)
    return answer

if __name__ == "__main__":
    n = 10000000000
    print(solution(n))