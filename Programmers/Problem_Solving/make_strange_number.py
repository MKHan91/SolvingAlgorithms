def solution(s):
    string_list = s.split(" ")
    for idx, string in enumerate(string_list):
        string_list[idx] = "".join([char.upper() if idx % 2 == 0 else char.lower() for idx, char in enumerate(string)])
    answer = " ".join(string_list)
    return answer

def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))

if __name__ == "__main__":
    s = "try hello world"
    print(solution(s))