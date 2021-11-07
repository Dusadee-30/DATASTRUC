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

q1_str = Queue()
q2_num = Queue()
q3_ascii = Queue()
q4_encode = Queue()
input_lst,num = input("Enter String and Code : ").split(",")
n = 0
j = 1
for i in input_lst:
    if(i != " "):
        q1_str.enQueue(i)
        n+=1
       
for i in num:
    q2_num.enQueue(int(i))
while j <= n:
    k = ""
    k = q1_str.deQueue()
    q1_str.enQueue(k)
    q3_ascii.enQueue(ord(k))
    j+=1
j = 1

num_last = 0
while j <= n:
    temp =0
    temp_2 =0
    k = int(q2_num.deQueue())
    temp_q2_num = k
    temp_q3_ascii = q3_ascii.deQueue()
    num_last = temp_q3_ascii+k
    q2_num.enQueue(k)
    if (num_last >= 65 and num_last <= 90) or (num_last >= 97 and num_last <= 122):
        q4_encode.enQueue(chr(num_last))
    if num_last< 65:
        temp = temp_q3_ascii-65
        temp_3 = temp_q2_num-temp
        num_last = 91-temp_3
        q4_encode.enQueue(chr(num_last))
    if num_last > 90 and temp_q3_ascii >= 65 and temp_q3_ascii <= 90:
        temp = 90-temp_q3_ascii
        temp_3 = temp_q2_num-temp
        num_last = 64+temp_3
        q4_encode.enQueue(chr(num_last))
    if num_last < 97 and temp_q3_ascii >= 97 and temp_q3_ascii <= 122:
        temp = temp_q3_ascii-97
        temp_3 = temp_q2_num-temp
        num_last = 123-temp_3
        q4_encode.enQueue(chr(num_last))
    if num_last > 122 :
        temp = 122-temp_q3_ascii
        temp_3 = temp_q2_num-temp
        num_last = 96+temp_3
        q4_encode.enQueue(chr(num_last))
       
    j+=1
   
print("Encode message is : ",q4_encode.items)
print("Decode message is : ",q1_str.items)



