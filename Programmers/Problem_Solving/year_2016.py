def solution(a, b):
    answer = ''
    weekend = ["FRI", "SAT", 'SUN', "MON", "TUE", "WED", "THU"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if a == 1:
        answer = weekend[(b-1)%7]
    else:
        answer = weekend[(sum(month[:a-1]) + ((b-1) % 7))%7]
    return answer

if __name__ == "__main__":
    a, b = 5, 24
    # a, b = 3, 15
    print(solution(a, b))