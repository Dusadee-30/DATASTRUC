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
    
    def nodeAt(self,i) :
        p = self.head                 
        for i in range(0,i) :
            p = p.next
        return p

    def search(self, item):
        p = self.head
        for i in range(len(self)) :
            if p.value == item :
                return p
            p = p.next
        return "Not Found"
    
    def index(self, item):
        q = self.head
        for i in range(len(self)):
            if q.value == item:
                return i
            q = q.next
        return "-1"

    def isEmpty(self):
        return self.head == None

    def removeNode(self,pos) :
        q = self.nodeAt(pos)
        p = self.nodeAt(pos-1)
        x = self.nodeAt(pos+1)
        p.next = x
        x.prev = p
        self.size -= 1

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
    
    def I_method(self,data):
        if(self.size == 1):
            p = self.Node(data)          
            self.head.prev = p
            p.next = self.head          
            self.head = p          
            self.size += 1
        else:
            a = self.search('|')
            p = self.Node(data)
            p = a.prev
            x = self.Node(data,p,a)
            p.next = a.prev = x
            self.size += 1
    def L_method(self):
        if self.index('|') == 0:
            []
        elif self.size == 2 and self.index('|') == 1:
            a = self.search('|')         
            p = a.prev
            x = self.Node(p.value)   
            self.head  = a
            a.next = x
            
        elif self.index('|') == self.size-1:
            a = self.search('|')     
            p = a.prev    
            q = p.prev 
            x = self.Node(p.value,a,None)
            q.next = a
            a.prev = q
            a.next = x 
            
           
        elif self.index('|') == 1:
            a = self.search('|')
            s = a.next
            p = a.prev   
            x = self.Node(p.value)             
            self.head = a
            a.prev = None
            a.next = x
            x.next = s  
            x.prev =a 
               
        else:
            a = self.search('|')    
            s = a.next 
            p = a.prev    
            q = p.prev            
            x = self.Node(p.value)
            q.next = a
            a.prev = q
            a.next = x
            x.next = s
            x.prev = a
            
    def R_method(self):
        if  self.index('|') == self.size-1:
            [] 
        elif self.index('|') == 0:
            a = self.search('|')              
            p = a.next                
            q = p.next 
            x = self.Node(p.value)
            self.head = x
            x.next = a
            a.next = q
            a.prev = x
            x.prev = None
                            
        else:
            a = self.search('|')  
            s = a.prev   
            p = a.next                
            q = p.next 
            x = self.Node(p.value)
            s.next = x
            x.next = a
            a.next = q
            a.prev = x
            x.prev = s
    def B_method(self)  :
        if self.index('|') != 0:
            a = self.search('|')
            p = a.prev            
            if self.index(p.value) == self.size-1:
                x = self.nodeAt(self.index(p.value))
                p = self.nodeAt(self.index(p.value)-1)
                self.tail = p
                p.next = None
                self.size -= 1
            elif self.index(p.value) == 0:
                self.head = self.head.next
                self.prev = None
                self.size -= 1
            else:
                self.removeNode(self.index(p.value))
        else:
            []
    def D_method(self):
        if self.index('|') != self.size-1:
            a = self.search('|')
            p = a.next            
            if self.index(p.value) == self.size-1:
                x = self.nodeAt(self.index(p.value))
                p = self.nodeAt(self.index(p.value)-1)
                self.tail = p
                p.next = None
                self.size -= 1
            elif self.index(p.value) == 0:
                self.head = self.head.next
                self.prev = None
                self.size -= 1
            else:
                self.removeNode(self.index(p.value))
            
        else:
            []
            
lst = LinkedList()
lst.append('|')
input_lst = input("Enter Input : ").split(",")
for i in input_lst:
    if i[:1] == 'I':
        lst.I_method(i[2:])
    if i[:1] == 'L':
        lst.L_method()
    if i[:1] == 'R':
        lst.R_method()
    if i[:1] == 'B':
        lst.B_method()
    if i[:1] == 'D':
        lst.D_method()
print(lst)