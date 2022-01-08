def solution(L, x, l, u):
    if not x in L:
        return - 1
    else:
        mid = (l + u) // 2
        if L[mid] == x:
            return mid
        elif x < L[mid]:
            u = mid - 1
            return solution(L, x, l, u)
        else:
            l = mid + 1
            return solution(L, x, l ,u)

if __name__ == "__main__":
    L = [2, 3, 5, 6, 9, 11, 15]
    x = 11
    l = 0
    u = 6
    print(solution(L, x, l, u))