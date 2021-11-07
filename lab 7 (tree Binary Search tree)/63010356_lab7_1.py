class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        n = Node(data)
        if self.root is None:
            self.root = n
        else:
            new = self.root
            while(True):
                if new.data > data:
                    if new.left is not None:
                        new = new.left                       
                    else:
                        new.left = n
                        break
                else:
                    if new.right is not None:
                        new = new.right              
                    else:
                        new.right = n
                        break
        return self.root
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()

inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)


