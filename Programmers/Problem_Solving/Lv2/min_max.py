def solution(s):
    integer_list = list(map(int, s.split(" ")))
    answer = " ".join([str(min(integer_list)), str(max(integer_list))])
    return answer

if __name__ == "__main__":
    s = "-1 -2 -3 -4"
    print(solution(s))