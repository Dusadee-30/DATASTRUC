class LinkedList :  
    class Node :
        def __init__(self,data,next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next
        
    def __init__(self):                
            self.dummy = self.Node(None,None)
            self.size = 0
            
    def __str__(self):
        s = 'link list : '
        p = self.dummy.next
        if p == None:
            return 'List is empty'
        while p != None :
            s += str(p.data) 
            p = p.next
            if p != None:
                s+='->'
        return s
          
    def __len__(self) :
        return self.size
            
    def isEmpty(self) :
        return self.size == 0
        
    def indexOf(self,data) :
        q = self.dummy.next
        for i in range(len(self)) :
            if q.data == data :
                return i
            q = q.next
        return "kaoyum"

    def check_index(self,num):
        q = self.dummy.next
        for i in range(len(self)):
            if i == num:
                return q.data
            q = q.next
        return "kaoyum"
            
    def isIn(self,data) :
        return self.indexOf(data) >= 0
    
    def nodeAt(self,i) :
        p = self.dummy
        for j in range(-1,i) :
            p = p.next
        return p
    
    def append(self,data) :
        return self.insertAfter(len(self),data)
    
    def insertAfter(self,i,data) :
        p = self.nodeAt(i-1)
        p.next = self.Node(data,p.next)
        self.size += 1
    
    def deleteAfter(self,i) :
        if self.size > 0 :
          p = self.nodeAt(i)
          p.next = p.next.next
          self.size -= 1
        
input_list = LinkedList()
decoy = LinkedList()
check_index = LinkedList()
data = LinkedList()
input_list = input("Enter Input : ").split(",")    
lst = LinkedList()
if input_list[0] != "" and input_list[0] != " ":
    for i in input_list[0].split(" "):
            lst.append(i)
input_list.pop(0)
for i in input_list:
    for j in i.split(":"):
        decoy.append(int(j))
for i in range(len(decoy)):
 
    if(i % 2 == 0):
        check_index.append(decoy.check_index(i))
    else:
        data.append(decoy.check_index(i))

print(lst)

for i in range(len(input_list)):
    if check_index.check_index(i) >= 0 and check_index.check_index(i) <= len(lst):
        lst.insertAfter(check_index.check_index(i),data.check_index(i))   
        print("index =",check_index.check_index(i) ,"and data =",data.check_index(i))
    else:
        print("Data cannot be added")
    print(lst)



    
    
           
     
          
    
