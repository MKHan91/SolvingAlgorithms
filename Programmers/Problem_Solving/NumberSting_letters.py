from ast import Num


def solution(s):
    NumberLetters_dict = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
                          "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9",
                          "ten": "10"}
    letters = ""
    answer = ""
    for char in s:
        if char.isdigit():
            answer += char
        else:
            letters += char
            if letters in NumberLetters_dict.keys():
                answer += NumberLetters_dict[letters]
                letters = ""

    return int(answer)

if __name__ == "__main__":
    s = "23four5six7"
    result = solution(s)
    print(result)