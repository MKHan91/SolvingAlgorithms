def solution(N, stages):
    answer = []
    fail_rate = []
    users = len(stages)
    for stage in range(1, N+1):
        if users == 0:
            fail_rate.append(0)
        else:
            fail_rate.append(stages.count(stage) / users)
            users -= stages.count(stage)

    num = 0
    while num != len(fail_rate):
        answer.append(fail_rate.index(max(fail_rate))+1)
        fail_rate[fail_rate.index(max(fail_rate))] = -1
        num += 1
    return answer

def solution2(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)

if __name__ == "__main__":
    # N = 4
    # stages = [4,4,4,4,4]
    # stages = [4,4,4,3,4]
    # N = 5
    # stages = [2, 1, 2, 6, 2, 4, 3, 3]
    N = 3
    stages = [1, 1, 1]
    print(solution2(N, stages))