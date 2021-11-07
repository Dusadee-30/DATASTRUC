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
class realStack:
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
lst_input = []
lst_decoy = []
S = Stack()
rs = realStack()
input_list = input("Enter Input : ").split(",")
for e in input_list:
  lst_input.append([i for i in e.split()])
#print(lst_input)
for i in lst_input:
    if i[0] == 'A':
        S.push(i[1])
        #print(S.items,"--->check push")
        rs.push(i[1])
    if i[0] == 'B':
        if(S.size() == 0):
            print(S.size())
        else:
         lst_decoy.append(S.pop())
         #print(lst_decoy,"---->dcoy first")
         for j in range(len(S.items)):
            if int(S.items[-1]) > int(lst_decoy[-1]):
                lst_decoy.append(S.pop())
                #print(lst_decoy,"---->check decoy")
            else:
                S.pop()
                #print(S.items,"--->check pop")
         for j in range(len(lst_decoy)):
                S.push(lst_decoy.pop()) 
         #print(S.items,"--->finish")
         print(S.size())
    if i[0] == 'S':
        for j in range(len(S.items)):
            S.pop()
        for f in range(len(rs.items)):
            lst_decoy.append(int(rs.pop()))
        for k in range(len(lst_decoy)):
            if lst_decoy[-1]%2 == 0:
                x = int(lst_decoy.pop())-1
                if(x < 1):
                    x = 1                
                S.push(x)
                rs.push(x)
                #print(S.items,"--->even number -1")
            else:
                x = int(lst_decoy.pop())+2            
                S.push(x)
                rs.push(x)
        #print(S.items,"---->after drunk")       




