def solution(L, x):
    answer = []
    if x in L:
        idx = L.index(x)
        answer.append(idx)
        for idx in answer:
            if idx+1 == len(L) :break
            try:
                answer.append(L[idx+1:].index(x) + idx+1)
            except ValueError:
                continue

    if not x in L:
        answer = [-1]
    
    return answer

if __name__ == "__main__":
    L = [64, 72, 85, 72, 54] 
    x = 72
    print(solution(L, x))