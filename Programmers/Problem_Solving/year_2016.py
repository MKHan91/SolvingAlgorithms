def solution(a, b):
    answer = ''
    week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", 'SUN']
    full = [1, 3, 5, 7, 8, 10, 12]
    not_full = [2, 4, 6, 9, 11]
    
    for month in range(1, 13):
        for day in range(1, 32):
            if month in full:
                print(week[(31 + 31 + 29 + 31 + 30)%7])
        a=1
    return answer

if __name__ == "__main__":
    a, b = 5, 24
    print(solution(a, b))