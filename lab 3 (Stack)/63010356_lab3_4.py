class Stack_del:
    def __init__(self,list = None):
        if list == None:
         self.items=[]
        else:
         self.items = list          
    def Add_del(self, i):
        self.items.append(i)
    def pop(self):            
        return self.items.pop()
    def size(self) :
        return len(self.items)    
    def del_num(self):
        return int(len(self.items))
       
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

lst_input = []
lst_decoy = []
S = Stack()
input_list = input("Enter Input : ").split(",")
for e in input_list:
  lst_input.append([i for i in e.split()])
#print(lst_input)
for i in lst_input:
    if i[0] == 'A':
        S.push(i[1])
        #print(S.items,"--->check push")
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
#print(S.items)

