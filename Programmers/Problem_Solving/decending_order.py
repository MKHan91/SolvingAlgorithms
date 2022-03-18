def solution(n):
    answer = int("".join(sorted(str(int(n)), reverse=True)))
    return answer

if __name__ == "__main__":
    n = 118372
    print(solution(n))