def solution(N, stages):
    answer = []
    fail_rate = []
    users = len(stages)
    for stage_num in range(1, N+1):
        fail_rate.append(stages.count(stage_num) / users)
        users -= stages.count(stage_num)

    num = 0
    while num != len(fail_rate):
        answer.append(fail_rate.index(max(fail_rate))+1)
        fail_rate[fail_rate.index(max(fail_rate))] = -1
        num += 1
    return answer

if __name__ == "__main__":
    N = 4
    # stages = [4,4,4,4,4]
    stages = [4,4,4,3,4]
    # N = 5
    # stages = [2, 1, 2, 6, 2, 4, 3, 3]
    print(solution(N, stages))