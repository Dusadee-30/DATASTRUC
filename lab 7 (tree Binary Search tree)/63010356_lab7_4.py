class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def setLevel(self, num):
        self.level = num

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None
        self.max_level = 0

    def insert(self, val):  
        self.max_level += 1
        if self.root == None:
            self.root = Node(val)
            self.root.level = 0
        else:
            check = self.root
            level = 0
            while True:
                if check.data < val:
                    if check.right:
                        check = check.right
                        level += 1
                    else:
                        level += 1
                        check.right = Node(val)
                        check.right.level = level
                        break
                elif check.data >= val:
                    if check.left:
                        check = check.left
                        level += 1
                    else:
                        level += 1
                        check.left = Node(val)
                        check.left.level = level
                        break
        return self.root
        
    def delete(self,root, data):
        check = root
        if check is None:
            print(f'Error! Not Found DATA')
        else:
            parent = None
            while True:
                if check is None:
                    print(f'Error! Not Found DATA')
                    break
                elif data > check.data:
                    parent = check
                    check = check.right
                elif data < check.data:
                    parent = check
                    check = check.left
                elif data == check.data:
                    if parent is None: 
                        parent = self.root
                        if check.right and check.left:
                            check = check.right
                            min_node, parent = checkLeftMin(check, parent)
                            temp = min_node.data 
                            if min_node.right:
                                self.delete(root,min_node)
                                self.root.data = temp
                                break
                            elif min_node.right is None:
                                if parent == self.root:
                                    parent.right = None
                                else:
                                    parent.left = None
                                self.root.data = temp
                                break
                        elif check.right or check.left:
                            if check.right:
                                check = check.right
                                self.root = check
                            elif check.left:
                                check = check.left
                                self.root = check 
                            break     
                        elif check.right is None and check.left is None:
                            self.root = None
                            break

                    else:
                        if check.right and check.left:
                            replace_node = check
                            check = check.right
                            min_node, parent = checkLeftMin(check, parent)
                            temp = min_node.data 
                            if min_node.right:
                                self.delete(root,min_node.data)
                                replace_node.data = temp
                                break
                            elif min_node.right is None: 
                                parent.left = None
                                replace_node.data = temp
                                break
                        elif check.right or check.left:#
                            if parent.right == check:
                                if check.right:
                                    check = check.right
                                    parent.right = check
                                elif check.left:
                                    check = check.left
                                    parent.right = check
                            elif parent.left == check:
                                if check.right:
                                    check = check.right
                                    parent.left = check
                                elif check.left:
                                    check = check.left
                                    parent.left = check
                            break 
                        elif check.right is None and check.left is None:
                            if parent.left == check:
                                parent.left = None
                            elif parent.right == check:
                                parent.right = None
                            break
        return self.root

def checkLeftMin(node, parent):
    check = node
    parent = parent
    while check.left:
        parent = check
        check = check.left
    return check,parent
    
def checkRightMost(node, parent):
    check = node
    parent = parent
    while check.right:
        parent = check
        check = check.right
    return check,parent

def printTree(node, level = 0):
    if node != None:
        printTree(node.right, level + 1)
        print('     ' * level, node)
        printTree(node.left, level + 1)

if __name__ == "__main__":
    tree = BinarySearchTree()
    data = input("Enter Input : ").split(",")
    for i in data:
        if i[0] == 'i':
            root = tree.insert(int(i[1:]))
            print(f'insert{i[1:]}')
            printTree(root)
        if i[0] == 'd':
            print(f'delete{i[1:]}')
            root = tree.root
            root = tree.delete(root, int(i[1:]))
            printTree(root)