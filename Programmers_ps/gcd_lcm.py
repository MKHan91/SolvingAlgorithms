def solution(n, m):
    share = []
    remain = [n, m]
    gcd = 1
    lcm = 1
    max(remain)
    for num in range(2, min(remain)+1):
        while True:
            if remain[0] % num == 0 and remain[1] % num == 0:
                remain[0] = remain[0] // num
                remain[1] = remain[1] // num
                share.append(num)
            else:
                break
    for ele in share:
        gcd *= ele
    for ele in remain:
        lcm *= ele
    answer = [gcd, gcd*lcm]
    return answer

def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer

if __name__ == "__main__":
    n, m = 3, 12
    # print(solution(n, m))
    print(gcdlcm(n, m))