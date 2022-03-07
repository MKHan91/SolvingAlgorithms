def solution(answers):
    answer = []
    pattern_cnt = list()
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    pattern = [a, b, c]
    for pt in pattern:
        answer_cnt = 0
        for num in range(len(answers)):
            if answers[num] == pt[num % len(pt)]:
                answer_cnt += 1
        pattern_cnt.append(answer_cnt)

    max_cnt, idx_max_cnt = max(pattern_cnt), pattern_cnt.index(max(pattern_cnt))
    answer.append(idx_max_cnt+1)
    for idx, pt_cnt in enumerate(pattern_cnt):
        if max_cnt == pt_cnt and idx != idx_max_cnt:
            answer.append(idx+1)

    return answer

if __name__ == "__main__":
    answers = [1, 3, 2, 4, 2]
    # answers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 5]
    print(solution(answers))