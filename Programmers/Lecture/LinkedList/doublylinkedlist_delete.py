from re import T


class Node:
    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None


    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr


    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):
        curr = prev.next
        prev.next = curr.next
        curr.next.prev = prev
        self.nodeCount -= 1
        return curr.data

    def popBefore(self, next):
        curr = next.prev
        prev = curr.prev
        
        prev.next = next
        next.prev = prev
        
        self.nodeCount -= 1
        return curr.data

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        if pos == self.nodeCount:
            prev = self.getAt(pos - 1)
            return self.popAfter(prev)
        
        next = self.getAt(pos + 1)
        return self.popBefore(next)


def solution(x):
    return 0

if __name__ == "__main__":
    DL = DoublyLinkedList()
    DL.nodeCount = 3
    
    DL1 = Node(67)
    DL2 = Node(50)
    DL3 = Node(43)
    
    DL1.prev = DL.head
    DL.head.next = DL1
    DL1.next = DL2
    DL2.prev = DL1
    DL2.next = DL3
    DL3.prev = DL2
    DL3.next = DL.tail
    DL.tail.prev = DL3
    
    print(DL.popAt(pos=0))