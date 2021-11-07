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

def postfixEval(st): 
    s = Stack()     
    for i in st: 
        if i in "+-*/": 
            operand2 = s.pop() 
            operand1 = s.pop() 
            result = doMath(i,operand1,operand2)
            s.push(result) 
        else: 
            s.push(int(i))
    return s.pop() 

def doMath(op, op1, op2): 
    if op == "*": 
        return op1 * op2 
    elif op == "/": 
        return op1 / op2 
    elif op == "+":  
        return op1 + op2 
    else: 
        return op1 - op2 

print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())

print("Answer : ",'{:.2f}'.format(postfixEval(token)))
