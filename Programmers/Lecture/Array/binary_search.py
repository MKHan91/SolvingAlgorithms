def solution(L, x):
    if x in L:
        lower = 0
        upper = len(L) - 1
        while lower <= upper:
            middle = (lower + upper) // 2
            if L[middle] < x:
                lower = middle + 1
            elif L[middle] > x:
                upper = middle
            elif L[middle] == x:
                answer = middle
                break
            
    elif not x in L:
        answer = -1
    return answer

if __name__ == "__main__":
    L = [2, 3, 5, 6, 9, 11, 15]
    x = 11
    print(solution(L, x))