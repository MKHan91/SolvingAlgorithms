def count_substring(string, sub_string):
    answer = []
    for cnt in range(len(string)-len(sub_string)+1):
        if string[cnt:len(sub_string)+cnt] == sub_string:
            answer += [string[cnt:len(sub_string)+cnt]]
    return len(answer)


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)