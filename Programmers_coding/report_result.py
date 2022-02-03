# 2022 카카오 블라인드 리쿠르팅 - 신고 결과 받기

def solution(id_list, report, k):
    reportList_dict = {} # 신고목록용 사전
    suspect_dict = {} # 피의자의 신고횟수 기록용 사전
    # suspect_list = [] # k번 이상 신고된 피의자들용 리스트
    mailCount_dict = {} # 신고자가 받은 메일의 횟수를 기록하기 위한 사전
    
    for user in id_list:
        reportList_dict[user] = []
        suspect_dict[user] = 0
        mailCount_dict[user] = 0
    
    for user in report:
        users = user.split(" ") # 신고자와 피의자 분리
        if users[1] in reportList_dict[users[0]]:
            continue
        reportList_dict[users[0]].append(users[1])
        suspect_dict[users[1]] += 1
        # if suspect_dict[users[1]] >= k:
        #     suspect_list.append(users[1])
    
    for key, value_list in reportList_dict.items():
        for value in value_list:
            if suspect_dict[value] >= k:
                mailCount_dict[key] += 1
    answer = list(mailCount_dict.values())
    return answer

def another_solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer
if __name__ == "__main__":
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    k = 2
    # id_list = ["con", "ryan"]
    # report = ["ryan con", "ryan con", "ryan con", "ryan con"]
    # k = 3
    print(solution(id_list, report, k))