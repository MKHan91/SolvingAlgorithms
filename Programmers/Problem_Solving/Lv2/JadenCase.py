def solution(s):
    s = s.lower()
    strings = s.split(" ")
    for idx, string in enumerate(strings):
        if string == '': continue
        if string[0].isalpha():
            strings[idx] = string[0].upper() + string[1:]
        else:
            continue
    answer = " ".join(strings)
    return answer

if __name__ == "__main__":
    s = "3pEopLe ssunFollowed me"
    print(solution(s))