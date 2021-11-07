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
        
    def height(self,node):
        if node is None:
            return -1 
        else :
            
            leftda = self.height(node.left)
            rightda = self.height(node.right)
 
            if (leftda > rightda):
                return leftda+1
            else:
                return rightda+1
            
        
T = BST()

inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
print("Height of this tree is :",T.height(root))