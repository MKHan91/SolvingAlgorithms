def solution(n, lost, reserve):
    answer = n - len(lost)
    reserve = sorted(reserve)
    lost = sorted(lost)
    
    intersection = set(lost) & set(reserve)
    for inter in intersection:
        reserve.remove(inter)
        lost.remove(inter)
    
    print(lost)
    print(reserve)
    for student in reserve:
        if student - 1 in lost:
            answer += 1
            lost.pop(lost.index(student-1))
        
        elif student + 1 in lost:
            answer += 1
            lost.pop(lost.index(student+1))
    
    return answer

if __name__ == "__main__":
    # n, lost, reserve = 5, [1, 2, 3, 4, 5], [1, 2, 3]
    # n, lost, reserve = 3, [1, 2], [2, 3]
    n, lost, reserve = 20, [4, 10, 6, 13, 14, 9], [3, 5, 8, 11, 12]
    # n, lost, reserve = 20, [1], [1, 2]
    # n, lost, reserve = 5, [4, 3], [3, 2]
    # n, lost, reserve = 3, [3], [1]
    print(solution(n, lost, reserve))