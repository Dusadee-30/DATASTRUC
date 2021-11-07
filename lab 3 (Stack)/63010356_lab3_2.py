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
    def Add(self, i):
        self.items.append(i)
    def pop(self):            
        return self.items.pop()
    def size(self) :
        return len(self.items)    
    def num(self):
        return int(len(self.items))
    
lst_input = []
lst_decoy = []
input_list = input("Enter Input : ").split(",")
for e in input_list:
  lst_input.append([i for i in e.split()])
n = len(lst_input)
i = 0
s = Stack()
d_s = Stack_del()
while i < n: 
    if lst_input[i][0] == "A":
        s.Add(int(lst_input[i][1]))
        d_s.Add_del(int(lst_input[i][1]))
        print("Add =",int(lst_input[i][1]))
    if lst_input[i][0] == "P":
        if(s.num() > 0):
            d_s.pop()
            print("Pop =",int(s.pop()))
        else:
            print("-1")
    if lst_input[i][0] == "D":
        k = 0
        o = 0     
        if(s.num() > 0):                        
            while k < d_s.del_num():
                if int(lst_input[i][1]) != d_s.items[-1-k]:
                    lst_decoy.append(s.items.pop())
                if int(lst_input[i][1]) == d_s.items[-1-k]:   
                    
                    print("Delete =",s.pop())            
                    o+=1                            
                k+=1 
            for j in range(len(lst_decoy)):
                    s.Add(lst_decoy.pop())  
   
            m = 0
            x = 0                     
            while m < (s.num()+o):
                d_s.pop()
                m+=1
            while x < s.num():
                d_s.Add_del(s.items[x])
                x+=1
                
        else:
            print("-1")
    if lst_input[i][0] == "LD":
        k = 0
        o = 0
        if(s.num() > 0):                        
            while k < d_s.del_num():
                if int(lst_input[i][1]) <= d_s.items[-1-k]:
                    lst_decoy.append(s.items.pop())
                if int(lst_input[i][1]) > d_s.items[-1-k]:   

                    print("Delete =",s.pop(),"Because",d_s.items[-1-k],"is less than",lst_input[i][1])
                    o+=1             
                k+=1    
            for j in range(len(lst_decoy)):
                    s.Add(lst_decoy.pop())  
  
            m = 0
            x = 0            
            while m < (s.num()+o):
                d_s.pop()
                m+=1
            while x < s.num():
                d_s.Add_del(s.items[x])
                x+=1
        else:
            print("-1")
    if lst_input[i][0] == "MD":
        k = 0
        o = 0
        if(s.num() > 0):                        
            while k < d_s.del_num():
                if int(lst_input[i][1]) >= d_s.items[-1-k]:
                    lst_decoy.append(s.items.pop())
                if int(lst_input[i][1]) < d_s.items[-1-k]:   

                    print("Delete =",s.pop(),"Because",d_s.items[-1-k],"is more than",lst_input[i][1])
                    o+=1             
                k+=1    
            for j in range(len(lst_decoy)):
                    s.Add(lst_decoy.pop())  
  
            m = 0
            x = 0            
            while m < (s.num()+o):
                d_s.pop()
                m+=1
            while x < s.num():
                d_s.Add_del(s.items[x])
                x+=1
        else:
            print("-1")
            
    i+=1

print("Value in Stack =",s.items)
