def solution(arr):
    answer = 1
    sorted_arr = sorted(arr)
    
    idx = 0
    min_value = sorted_arr[0]
    queue = []
    while idx != len(sorted_arr)-1:
        a = sorted_arr[idx+1]
        
        remain = a % min_value
        if remain == 0:
            answer *= (a // min_value)
            idx += 1
        else:
            queue.append(a)
            idx += 1
            if idx == len(sorted_arr)-1:
                answer *= min_value
                min_value = queue.pop(0)
                idx -= 1

    if len(queue) != 0:
        answer *= queue.pop(0)
    answer *= min_value
    return answer

if __name__ == "__main__":
    arr = [2,6,7,14]
    # arr = [2,6,7,8]
    # arr = [1, 2, 3]
    print(solution(arr))