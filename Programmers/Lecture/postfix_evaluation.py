from cv2 import exp
from numpy import multiply


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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []
    for token in tokenList:
        if type(token) is int:
            postfixList.append(token)

        elif token == "(":
            opStack.push(token)
            
        elif token == ")":
            while opStack.peek() != "(":
                postfixList.append(opStack.pop())
            opStack.pop()
            
        else:
            if opStack.isEmpty():
                opStack.push(token)
            else:
                if prec[opStack.peek()] >= prec[token]:
                    postfixList.append(opStack.pop())
                opStack.push(token)
                    
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
        
    return postfixList


def postfixEval(tokenList):
    opStack = ArrayStack()
    for token in tokenList:
        answers = []
        if type(token) is int:
            opStack.push(token)
            
        elif type(token) is str:
            while True:
                answers.append(opStack.pop())
                if len(answers) == 2:
                    break
            
            if token == "+":
                val = sum(answers)
            elif token == "-":
                val = answers[1] - answers[0]
            elif token == "*":
                val = answers[1] * answers[0]
            elif token == "/":
                val = answers[1] / answers[0]
            opStack.push(val)

    return opStack.peek()

def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val

if __name__ == "__main__":
    expression = "10+(100-20-1)"
    result = solution(expr=expression)
    print(result)