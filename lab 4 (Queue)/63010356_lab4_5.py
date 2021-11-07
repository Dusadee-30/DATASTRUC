class Queue:  
    def __init__(self, list = None) :
        if list == None:
            self.items = []
        else :
            self.items = list
    def enQueue(self,i):
        self.items.append(i)       
    def deQueue(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items == []
class Stack:   
    def __init__(self,list = None):
        if list == None:
         self.items=[]
        else:
         self.items = list         
    def push(self, i):
        self.items.append(i)
    def pop(self):            
        return self.items.pop()
    def size(self) :
        return len(self.items)    
    def num(self):
        return int(len(self.items))
    def peek(self):
        return self.items[-1]
q_normol = Queue()
q_normol_decoy = Stack()
q_mirror = Stack()
q_mirror_decoy = Stack()
q_mirror_output = Queue()
bomb = Queue()
n_normol = 0
n_mirror = 0
j = 0
k = 0
input_normol,input_mirror = input("Enter Input (Normal, Mirror) : ").split(" ")
for i in input_normol:
    q_normol.enQueue(i)
    n_normol+=1
for i in input_mirror:
    q_mirror.push(i)
    n_mirror+=1
while k < n_mirror:
    x = q_mirror.pop()       
    if k > 1 and q_mirror_decoy.size() > 1:        
        if q_mirror_decoy.items[-1] == x and q_mirror_decoy.items[-2] == x :
            q_mirror_decoy.pop()
            q_mirror_decoy.pop()  
            bomb.enQueue(x)      
        else:
            q_mirror_decoy.push(x)
    else:
        q_mirror_decoy.push(x)             
    k+=1
num_bomb = bomb.size()
c = 0

bombfail = 0
while j < n_normol:
    x = q_normol.deQueue()       
    if j > 1 and q_normol_decoy.size() > 1:        
        if q_normol_decoy.items[-1] == x and q_normol_decoy.items[-2] == x :           
            if(bomb.size() > 0):
                bomber = bomb.deQueue()
                if q_normol_decoy.items[-1] == bomber and q_normol_decoy.items[-2] == bomber:
                    q_normol_decoy.pop()
                    q_normol_decoy.pop()
                    q_normol_decoy.push(x)
                    bombfail += 1
                else:
                    q_normol_decoy.push(bomber)
                    q_normol_decoy.push(x)
            elif q_normol_decoy.items[-1] == x and q_normol_decoy.items[-2] == x :
                q_normol_decoy.pop()
                q_normol_decoy.pop()      
                c+=1  
        else:
            q_normol_decoy.push(x)
    else:
        q_normol_decoy.push(x)             
    j+=1
z = q_normol_decoy.size()
z2 = q_mirror_decoy.size()
w = 0
w2 = 0
while w < z:
    q_normol.enQueue(q_normol_decoy.pop())
    
    w+=1
while w2 <z2:
    q_mirror_output.enQueue(q_mirror_decoy.pop())
    w2+=1

print("NORMAL :")
print(z)
if(q_normol.size() != 0):
    print("".join(q_normol.items))
else:
    print("Empty")
print(c,"Explosive(s) ! ! ! (NORMAL)")
if(bombfail != 0):
    if(bombfail > 1):
        print("Failed Interrupted",bombfail,"Bomb(s)")
    else:
        print("Failed Interrupted",bombfail,"Bomb")
print("------------MIRROR------------")
print(": RORRIM")
print(q_mirror_output.size())
if(q_mirror_output.size() != 0):
    print("".join(q_mirror_output.items))
else:
    print("ytpmE")
print("(RORRIM) ! ! ! (s)evisolpxE",num_bomb)

