class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def insert(self, key, data):
        if key < self.key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left = Node(key, data)

        elif key > self.key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right = Node(key, data)

        else:
            raise KeyError
        
    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal

class BinSearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

def solution(x):
    return 0

if __name__ == "__main__":
    a = Node(key=5, data="John")
    b = Node(key=2, data="David")
    c = Node(key=8, data="Mary")
    d = Node(key=1, data="Patrick")
    e = Node(key=4, data="Sue")
    f = Node(key=6, data="Anne")
    g = Node(key=9, data="Clara")
    h = Node(key=7, data="Peter")
    
    a.left, a.right = b, c
    b.left, b.right = d, e
    c.left, c.right = f, g
    f.right = h
    
    BST = BinSearchTree()
    BST.root = a
    BST.insert(key=3, data="Kevin")