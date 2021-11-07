class LinkedList:
    class Node:
        def __init__(self, value,prev = None,next = None):
            self.value = value
            if prev is None :
                self.prev = None
            else :
                self.prev = prev

            if next is None :
                self.next = None
            else :
                self.next = next
    def __init__(self):   
        self.head = None
        self.tail = None
        
        self.size = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s
    
    def __len__(self) :               
        return self.size 

    def reverse(self): 

        if(self.isEmpty()):
            return "Empty"
        else:
            
            current = self.head;              
            while(current != None):    
                temp = current.next;    
                current.next = current.prev;    
                current.prev = temp;    
                current = current.prev;                
            temp = self.head;    
            self.head = self.tail;    
            self.tail = temp;    
            current = self.head;     
            if(self.head == None):    
                print("List is empty");    
                return;    
            s = current.value+" "
            current = current.next
            while(current != None):     
                s += str(current.value)+" " 
                current = current.next
            return s

    def nodeAt(self,i) :
        p = self.head
        if i < 0:
            i = int(i) + int(self.size)            
        for j in range(0,i) :
            p = p.next
        return p

    def isEmpty(self):
        return self.head == None

    def append(self, data):         
        #Create a new node    
        newNode = self.Node(data)    
            
        #If list is empty    
        if(self.head == None):       
            self.head = self.tail = newNode                    
            self.size += 1  
        else:    
              
            self.tail.next = newNode      
            newNode.prev = self.tail       
            self.tail = newNode                     
            self.size += 1
  
    def addHead(self,data) :
        if self.isEmpty() :
          p = self.Node(data)
          self.head  = self.tail = p
          #self.head = self.Node(data,None)
          self.size += 1
        else :
          p = self.Node(data)          
          self.head.prev = p
          p.next = self.head          
          self.head = p          
          self.size += 1   
   
    def insert(self,i,data) :
        if self.isEmpty() :
            p = self.Node(data)
            self.head = self.tail = p
            self.size += 1
        elif i >= self.size-1:
            newNode = self.Node(data)                
            #If list is empty    
            if(self.head == None):       
                self.head = self.tail = newNode                    
                self.size += 1  
            else:                 
                self.tail.next = newNode      
                newNode.prev = self.tail       
                self.tail = newNode                     
                self.size += 1
        elif int(i) + int(self.size) < 0:
            if self.isEmpty() :
                p = self.Node(data)
                self.head  = self.tail = p
                #self.head = self.Node(data,None)
                self.size += 1
            else:
                p = self.Node(data)          
                self.head.prev = p
                p.next = self.head          
                self.head = p          
                self.size += 1
        else:
            a = self.nodeAt(i)
            p = self.Node(data)
            p = a.prev
            x = self.Node(data,p,a)
            p.next = a.prev = x
            self.size += 1
            
    def search(self, item):
        p = self.head
        for i in range(len(self)) :
            if p.value == item :
                return "Found"
            p = p.next
        return "Not Found"

    def index(self, item):
        q = self.head
        for i in range(len(self)):
            if q.value == item:
                return i
            q = q.next
        return "-1"

    def removeNode(self,pos) :
        q = self.nodeAt(pos)
        p = self.nodeAt(pos-1)
        x = self.nodeAt(pos+1)
        p.next = x
        x.prev = p
        self.size -= 1
    
    def pop(self, pos):
        if self.size > 0 and pos < len(self) and pos >= 0:
            if pos == 0 :
                self.head = self.head.next
                self.prev = None
                self.size -= 1
                return "Success"
            elif pos == len(self)-1 :
                
                x = self.nodeAt(pos)
                p = self.nodeAt(pos-1)
                self.tail = p
                p.next = None
                self.size -= 1
                return "Success"
            else:
                self.removeNode(pos)  
                return "Success"
        else:
          return("Out of Range")

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(len(L), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])

print("Linked List :", L)
print("Linked List Reverse :", L.reverse())
