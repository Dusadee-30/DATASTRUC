class Stack:   
    def __init__(self,list = None):
        if list == None:
         self.items=[]
        else:
         self.items = list      
        
    def push(self, i):
        self.items.append(i)
    def pop(self):   #edit code          
        return self.items.pop()
    def size(self) :
        return len(self.items)
    
    def num(self):
        return int(len(self.items))
    
    

lst_input = []

input_list = input("Enter Input : ").split(",")

for e in input_list:

  lst_input.append([i for i in e.split()])
n = len(lst_input)
s = Stack()
i = 0
while i < n:   
    if lst_input[i][0] == "P":
     if(s.num() > 0 ):
      print("Pop =",s.pop(),"and Index =",s.size())
     else:
      print("-1")     
    if lst_input[i][0] == "A":
        s.push(lst_input[i][1])    
        print("Add =",lst_input[i][1], "and Size =",s.size())
    i+=1
if(s.num() != 0):
 print("Value in Stack =",*s.items)
else:
 print("Value in Stack = Empty")