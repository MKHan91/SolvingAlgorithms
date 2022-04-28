def solution(L, x):
    for idx, element in enumerate(L):
        if element > x and idx == 0:
            L.insert(idx, x)
            break
        if element > x and idx != 0:
            L.insert(idx, x)
            break
        if element < x and idx == len(L)-1:
            L.insert(idx+1, x)
            break
    answer = L
    return answer

if __name__ == '__main__':
    L = [20, 37, 58, 72, 91]
    x = 95
    
    answer = solution(L, x)
    print(answer)