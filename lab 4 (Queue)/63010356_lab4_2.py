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
main = Queue()
x = 1
s1 = Queue()
s2 = Queue()
input_lst,time = input("Enter people and time : ").split(" ")
time_int = int(time)
for i in input_lst:
    main.enQueue(i)
while x <= time_int:
    if (x-1)%3 == 0 and s1.isEmpty() == False:
            s1.deQueue()
    if x >= 10 and x%2 == 0 and s1.isEmpty() == False :
            s2.deQueue()
    if s1.size() < 5 :
               
        if main.isEmpty() == False:
            s1.enQueue(main.deQueue())
            print(x,main.items,s1.items,s2.items,)
        else:
            print(x,main.items,s1.items,s2.items,)
        
    else:
        
        if main.isEmpty() == False:
            s2.enQueue(main.deQueue())
            print(x,main.items,s1.items,s2.items)
        else:
            print(x,main.items,s1.items,s2.items)
    x+=1