def solution(num):
    answer = ""
    if num % 2 != 0:
        answer += "Odd"
    else:
        answer += "Even"
    return answer

if __name__ == "__main__":
    num = 3
    print(solution(num))