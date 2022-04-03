class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal

    def postorder(self):
        traversal = []
        if self.left:
            traversal += self.left.postorder()
        if self.right:
            traversal += self.right.postorder()
        
        traversal.append(self.data)
        return traversal

class BinaryTree:
    def __init__(self, r):
        self.root = r

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

    def postorder(self):
        if self.root:
            return self.root.postorder()
        else:
            return []

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
    
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    
    print(a.postorder())