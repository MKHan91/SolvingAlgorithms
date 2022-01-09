class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        # self.nodeCount = 3
        # self.head = Node(67)
        # self.tail = Node(58)
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def traverse(self):
        answer = []
        curr = self.head
        while curr != None:
            answer.append(curr.data)
            curr = curr.next
        
        return answer
        # answer = []
        # if self.head == None and self.tail == None and self.nodeCount == 0:
        #     return answer
        # else:
        #     self.head.next = Node(34)
        #     self.head.next.next = self.tail
        #     self.tail.next = None
        #     for cnt in range(1, self.nodeCount+1):
        #         curr = self.getAt(pos=cnt)
        #         answer.append(curr.data)
        # return answer


# 이 solution 함수는 그대로 두어야 합니다.
def solution(x):
    return 0

if __name__ == "__main__":
    linked_list = LinkedList()
    answer = linked_list.traverse()
    print(answer)