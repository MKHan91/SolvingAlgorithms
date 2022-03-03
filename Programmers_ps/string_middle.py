def solution(s):
    answer = ''
    if len(s)%2 == 0:
        answer = s[len(s)//2-1:len(s)//2+1]
    else:
        answer = s[len(s)//2]
        
    return answer

def solution2(s):
    print(s)
    return s[(len(s)-1)//2:len(s)//2+1]
if __name__ == "__main__":
    s = "abcdef"
    print(solution2(s))