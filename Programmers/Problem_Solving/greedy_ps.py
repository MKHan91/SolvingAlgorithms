def solution(n, lost, reserve):
    answer = n - len(lost)
    reserve = sorted(reserve)
    lost = sorted(lost)
    
    for student in lost[:]:
        if student in reserve:
            reserve.remove(student)
            lost.remove(student)
            answer += 1
            continue
        
        if student - 1 in reserve:
            if student in reserve:
                continue
            answer += 1
            reserve.remove(student-1)
        
        elif student + 1 in reserve:
            if student + 1 in lost:
                continue
            else:
                answer += 1
                reserve.remove(student+1)
            
    return answer
    

if __name__ == "__main__":
    # n, lost, reserve = 5, [1, 2, 3, 4, 5], [1, 2, 3]
    # n, lost, reserve = 3, [1, 2], [2, 3]
    # n, lost, reserve = 3, [1, 2], [1, 3, 2]
    # n, lost, reserve = 20, [4, 10, 6, 13, 14, 9], [3, 5, 8, 11, 12]
    # n, lost, reserve = 20, [1], [1, 2]
    # n, lost, reserve = 5, [4, 3], [3, 2]
    n, lost, reserve = 5, [4, 3], [2, 3]
    
    # n, lost, reserve = 3, [3], [1]
    print(solution(n, lost, reserve))