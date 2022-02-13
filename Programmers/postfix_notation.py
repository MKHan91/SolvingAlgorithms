class ArrayStack:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    answer = ''
    opStack = ArrayStack()
    for char in S:
        if char == "(":
            opStack.push(char)
        
        elif char == "+" or char == "*" or char == "/" or char == "-":
            if opStack.isEmpty():
                opStack.push(char)
            else:
                if opStack.data[-1] == "(":
                    opStack.pop()
                    opStack.push(char)
                else:
                    if prec[opStack.peek()] >= prec[char]:
                        answer += opStack.pop()
                        opStack.push(char)
                    elif prec[opStack.peek()] < prec[char]:
                        # answer += char
                        opStack.push(char)
                    # else:
                    #     answer += opStack.pop()
                    #     opStack.push(char)
        elif char == ")":
            answer += opStack.pop()
        else:
            answer += char

    while not opStack.isEmpty():
        if opStack.data[-1] == "(":
            opStack.pop()
        else:
            answer += opStack.pop()
    return answer

if __name__ == "__main__":
    S = "A*(B-(C+D))"
    result = solution(S)
    print(result)