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
lst_1 = LinkedList()
lst_2 = LinkedList()
input_lst,input_lst2 = input("Enter Input (L1,L2) : ").split(" ")
for i in input_lst.split('->'):
    lst_1.append(i)
for i in input_lst2.split('->'):
    lst_2.append(i)
print("L1    :",lst_1)
print("L2    :",lst_2)
print("Merge :",str(lst_1)+lst_2.reverse())
  
    
    
            
    

    

    
    
    