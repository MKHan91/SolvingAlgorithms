# 재귀 함수를 이용한 gcd 구하기. 
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a, b):
    max_value, min_value = max(a, b), min(a, b)
    remain = 1
    while remain > 0:
        remain = max_value % min_value
        max_value, min_value = min_value, remain
    
    lcm = a*b//max_value
    return lcm 

def solution(arr):
    arr = sorted(arr)

    while len(arr) >= 2:
        a, b = arr.pop(0), arr.pop(0)
        arr.insert(0, lcm(a, b))
    answer = arr[0]
    return answer

if __name__ == "__main__":
    arr = [2,6,7,14]
    # arr = [2,6,8,14]
    # arr = [1, 2, 3]
    print(solution(arr))