from tkinter.messagebox import NO
from turtle import pos


class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.nodeCount = 6
        # self.head = None
        # self.tail = None
        self.head = Node(67)
        self.tail = Node(43)

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        
        curr = self.getAt(pos)
        if self.nodeCount == 1:
            self.head = None
            self.tail = None
            curr.data = None
            
        elif pos == 1:
            self.head = curr.next
            
        elif pos == self.nodeCount:
            prev = self.getAt(pos-1)
            prev.next = curr.next
            self.tail = prev

        else:
            prev = self.getAt(pos-1)
            prev.next = curr.next
                
        self.nodeCount -= 1
        return curr.data

    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result
    
    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


def solution(x):
    return 0

if __name__ == "__main__":
    L = LinkedList()
    a = Node(13)
    # b = Node(27)
    # c = Node(29)
    L.head = a
    # L.tail = c
    # L.nodeCount = 3
    L.nodeCount = 1
    # a.next = b
    # b.next = c
    L.popAt(pos=2)
    