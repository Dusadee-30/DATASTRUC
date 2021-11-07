class Queue:
   
    def __init__(self, list = None) :
        if list == None:
            self.items = []
        else :
            self.items = list
    def enQueue(self,i):
        self.items.append(i)      
        return self.items.index(i)  
    def deQueue(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    
        
lst_input = []
q = Queue()
input = input("Enter Input : ").split(",")
for e in input:
    lst_input.append([i for i in e.split()])
for i in lst_input:
    if(i[0] == "E"):        
        print("Add",i[1],"index is",q.enQueue(i[1]))
    if(i[0]=="D"):
        if(q.size() == 0):
            print("-1")
        else:
            print("Pop",q.deQueue(),"size in queue is",q.size())
if(q.size() == 0):
    print("Empty")
else:
    print("Number in Queue is : ",q.items)
