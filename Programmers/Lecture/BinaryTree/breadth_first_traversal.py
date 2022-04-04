class ArrayQueue:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]

class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, r):
        self.root = r

    def bft(self):
        q = ArrayQueue()
        traversal = []
        
        if self.root:
            q.enqueue(self.root)
            
        while not q.isEmpty():
            node = q.dequeue()
            traversal.append(node.data)
            print(traversal)
            if node.left:
                q.enqueue(node.left)
                if node.right:
                    q.enqueue(node.right)

            elif node.right:
                q.enqueue(node.right)
                if node.left:
                    q.enqueue(node.left)
        return traversal
        
def solution(x):
    return 0

if __name__ == "__main__":
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")
    f = Node("F")
    g = Node("G")
    h = Node("H")
    j = Node("J")
    
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    d.left = h
    f.right = j
    
    bt = BinaryTree(r=a)
    bt.bft()