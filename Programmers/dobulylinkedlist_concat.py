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


    def concat(self, L):
        target1 = L.head.next
        target1.prev = self.tail.prev
        self.tail.prev.next = target1
        target2 = L.tail.prev
        target2.next = self.tail
        self.tail.prev = target2
        
        self.nodeCount += L.nodeCount

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


def solution(x):
    return 0

if __name__ == "__main__":
    DL1 = DoublyLinkedList()
    DL1.nodeCount = 3
    DL2 = DoublyLinkedList()
    DL2.nodeCount = 2
    
    DL1_1 = Node(67)
    DL1_2 = Node(53)
    DL1_3 = Node(43)
    
    DL2_1 = Node(30)
    DL2_2 = Node(20)
    
    DL1.head.next = DL1_1
    DL1_1.prev = DL1.head
    DL1_1.next = DL1_2
    DL1_2.prev = DL1_1
    DL1_2.next = DL1_3
    DL1_3.prev = DL1_2
    DL1_3.next = DL1.tail
    DL1.tail.prev = DL1_3
    
    DL2.head.next = DL2_1
    DL2_1.prev = DL2.head
    DL2_1.next = DL2_2
    DL2_2.prev = DL1_1
    DL2_2.next = DL2.tail
    DL2.tail.prev = DL2_2
    
    DL1.concat(DL2)