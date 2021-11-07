
class node():
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class linklist():
    def __init__(self):
        self.head=None
        self.tail=None
    def append(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
        else:
            self.tail.next=newnode
        self.tail=newnode
    def __str__(self):
        if self.head is None:
            return ""
        temp=str(self.head.data)
        last=self.head
        while (last.next is not None):
            temp=temp+" "+str(last.next.data)
            last=last.next
        return temp
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
    def dequeue(self):
        temp=self.head.data
        self.head=self.head.next
        return temp
    def size(self):
        size=0
        last=self.head
        while last is not None:
            last=last.next
            size=size+1
        return  size
    def sort(self):
        for i in range(self.size()-1):
            last=self.head
            while last.next is not None:
                if last.data < last.next.data:
                    temp=last.data
                    last.data=last.next.data
                    last.next.data=temp
                last=last.next
    def result(self):
        if self.head is None:
            return ""
        temp=str(self.head.data)
        last=self.head
        while (last.next is not None):
            temp=temp+" -> "+str(last.next.data)
            last=last.next
        return temp

if __name__=="__main__":
    inp=input("Enter Input : ").split()
    ll=linklist()
    lloriginal=linklist()
    for i in inp:
        ll.append(i)
        lloriginal.append(i)
    l0=linklist()
    l1=linklist()
    l2=linklist()
    l3=linklist()
    l4=linklist()
    l5=linklist()
    l6=linklist()
    l7=linklist()
    l8=linklist()
    l9=linklist()
    divider=1
    round=1
    while not ll.isEmpty():
        value=int(ll.dequeue())
        if value<0:
            decoy=(0-value)%10
        else:
            decoy=value%10
        if decoy==0:
            l0.append(value)
        elif decoy==1:
            l1.append(value)
        elif decoy==2:
            l2.append(value)
        elif decoy==3:
            l3.append(value)
        elif decoy==4:
            l4.append(value)
        elif decoy==5:
            l5.append(value)
        elif decoy==6:
            l6.append(value)
        elif decoy==7:
            l7.append(value)
        elif decoy==8:
            l8.append(value)
        elif decoy==9:
            l9.append(value)
    l0.sort()
    l1.sort()
    l2.sort()
    l3.sort()
    l4.sort()
    l5.sort()
    l6.sort()
    l7.sort()
    l8.sort()
    l9.sort()
    while (True):
        print("------------------------------------------------------------")
        print("Round : {}".format(round))
        print("0 :",l0)
        print("1 :",l1)
        print("2 :",l2)
        print("3 :",l3)
        print("4 :",l4)
        print("5 :",l5)
        print("6 :",l6)
        print("7 :",l7)
        print("8 :",l8)
        print("9 :",l9)
        if(l1.isEmpty() and l2.isEmpty() and l3.isEmpty() and l4.isEmpty() and l5.isEmpty() and l6.isEmpty() and l7.isEmpty() and l8.isEmpty() and l9.isEmpty()):
            break
        ######################################################################
        round=round+1
        divider=divider*10
        l0_new=linklist()
        l1_new=linklist()
        l2_new=linklist()
        l3_new=linklist()
        l4_new=linklist()
        l5_new=linklist()
        l6_new=linklist()
        l7_new=linklist()
        l8_new=linklist()
        l9_new=linklist()
        #
        while not l0.isEmpty():
            value=int(l0.dequeue())
            if value<0:
                decoy=(0-int(value/divider))%10
            else:
                decoy=int(value/divider)%10
            if decoy==0:
                l0_new.append(value)
            elif decoy==1:
                l1_new.append(value)
            elif decoy==2:
                l2_new.append(value)
            elif decoy==3:
                l3_new.append(value)
            elif decoy==4:
                l4_new.append(value)
            elif decoy==5:
                l5_new.append(value)
            elif decoy==6:
                l6_new.append(value)
            elif decoy==7:
                l7_new.append(value)
            elif decoy==8:
                l8_new.append(value)
            elif decoy==9:
                l9_new.append(value)
        while not l1.isEmpty():
            value=int(l1.dequeue())
            if value<0:
                decoy=(0-int(value/divider))%10
            else:
                decoy=int(value/divider)%10
            if decoy==0:
                l0_new.append(value)
            elif decoy==1:
                l1_new.append(value)
            elif decoy==2:
                l2_new.append(value)
            elif decoy==3:
                l3_new.append(value)
            elif decoy==4:
                l4_new.append(value)
            elif decoy==5:
                l5_new.append(value)
            elif decoy==6:
                l6_new.append(value)
            elif decoy==7:
                l7_new.append(value)
            elif decoy==8:
                l8_new.append(value)
            elif decoy==9:
                l9_new.append(value)
        while not l2.isEmpty():
            value=int(l2.dequeue())
            if value<0:
                decoy=(0-int(value/divider))%10
            else:
                decoy=int(value/divider)%10
            if decoy==0:
                l0_new.append(value)
            elif decoy==1:
                l1_new.append(value)
            elif decoy==2:
                l2_new.append(value)
            elif decoy==3:
                l3_new.append(value)
            elif decoy==4:
                l4_new.append(value)
            elif decoy==5:
                l5_new.append(value)
            elif decoy==6:
                l6_new.append(value)
            elif decoy==7:
                l7_new.append(value)
            elif decoy==8:
                l8_new.append(value)
            elif decoy==9:
                l9_new.append(value)
        while not l3.isEmpty():
            value=int(l3.dequeue())
            if value<0:
                decoy=(0-int(value/divider))%10
            else:
                decoy=int(value/divider)%10
            if decoy==0:
                l0_new.append(value)
            elif decoy==1:
                l1_new.append(value)
            elif decoy==2:
                l2_new.append(value)
            elif decoy==3:
                l3_new.append(value)
            elif decoy==4:
                l4_new.append(value)
            elif decoy==5:
                l5_new.append(value)
            elif decoy==6:
                l6_new.append(value)
            elif decoy==7:
                l7_new.append(value)
            elif decoy==8:
                l8_new.append(value)
            elif decoy==9:
                l9_new.append(value)
        while not l4.isEmpty():
            value=int(l4.dequeue())
            if value<0:
                decoy=(0-int(value/divider))%10
            else:
                decoy=int(value/divider)%10
            if decoy==0:
                l0_new.append(value)
            elif decoy==1:
                l1_new.append(value)
            elif decoy==2:
                l2_new.append(value)
            elif decoy==3:
                l3_new.append(value)
            elif decoy==4:
                l4_new.append(value)
            elif decoy==5:
                l5_new.append(value)
            elif decoy==6:
                l6_new.append(value)
            elif decoy==7:
                l7_new.append(value)
            elif decoy==8:
                l8_new.append(value)
            elif decoy==9:
                l9_new.append(value)
        while not l5.isEmpty():
            value=int(l5.dequeue())
            if value<0:
                decoy=(0-int(value/divider))%10
            else:
                decoy=int(value/divider)%10
            if decoy==0:
                l0_new.append(value)
            elif decoy==1:
                l1_new.append(value)
            elif decoy==2:
                l2_new.append(value)
            elif decoy==3:
                l3_new.append(value)
            elif decoy==4:
                l4_new.append(value)
            elif decoy==5:
                l5_new.append(value)
            elif decoy==6:
                l6_new.append(value)
            elif decoy==7:
                l7_new.append(value)
            elif decoy==8:
                l8_new.append(value)
            elif decoy==9:
                l9_new.append(value)
        while not l6.isEmpty():
            value=int(l6.dequeue())
            if value<0:
                decoy=(0-int(value/divider))%10
            else:
                decoy=int(value/divider)%10
            if decoy==0:
                l0_new.append(value)
            elif decoy==1:
                l1_new.append(value)
            elif decoy==2:
                l2_new.append(value)
            elif decoy==3:
                l3_new.append(value)
            elif decoy==4:
                l4_new.append(value)
            elif decoy==5:
                l5_new.append(value)
            elif decoy==6:
                l6_new.append(value)
            elif decoy==7:
                l7_new.append(value)
            elif decoy==8:
                l8_new.append(value)
            elif decoy==9:
                l9_new.append(value)
        while not l7.isEmpty():
            value=int(l7.dequeue())
            if value<0:
                decoy=(0-int(value/divider))%10
            else:
                decoy=int(value/divider)%10
            if decoy==0:
                l0_new.append(value)
            elif decoy==1:
                l1_new.append(value)
            elif decoy==2:
                l2_new.append(value)
            elif decoy==3:
                l3_new.append(value)
            elif decoy==4:
                l4_new.append(value)
            elif decoy==5:
                l5_new.append(value)
            elif decoy==6:
                l6_new.append(value)
            elif decoy==7:
                l7_new.append(value)
            elif decoy==8:
                l8_new.append(value)
            elif decoy==9:
                l9_new.append(value)
        while not l8.isEmpty():
            value=int(l8.dequeue())
            if value<0:
                decoy=(0-int(value/divider))%10
            else:
                decoy=int(value/divider)%10
            if decoy==0:
                l0_new.append(value)
            elif decoy==1:
                l1_new.append(value)
            elif decoy==2:
                l2_new.append(value)
            elif decoy==3:
                l3_new.append(value)
            elif decoy==4:
                l4_new.append(value)
            elif decoy==5:
                l5_new.append(value)
            elif decoy==6:
                l6_new.append(value)
            elif decoy==7:
                l7_new.append(value)
            elif decoy==8:
                l8_new.append(value)
            elif decoy==9:
                l9_new.append(value)
        while not l9.isEmpty():
            value=int(l9.dequeue())
            if value<0:
                decoy=(0-int(value/divider))%10
            else:
                decoy=int(value/divider)%10
            if decoy==0:
                l0_new.append(value)
            elif decoy==1:
                l1_new.append(value)
            elif decoy==2:
                l2_new.append(value)
            elif decoy==3:
                l3_new.append(value)
            elif decoy==4:
                l4_new.append(value)
            elif decoy==5:
                l5_new.append(value)
            elif decoy==6:
                l6_new.append(value)
            elif decoy==7:
                l7_new.append(value)
            elif decoy==8:
                l8_new.append(value)
            elif decoy==9:
                l9_new.append(value)
        l0=l0_new
        l1=l1_new
        l2=l2_new
        l3=l3_new
        l4=l4_new
        l5=l5_new
        l6=l6_new
        l7=l7_new
        l8=l8_new
        l9=l9_new
        l0.sort()
        l1.sort()
        l2.sort()
        l3.sort()
        l4.sort()
        l5.sort()
        l6.sort()
        l7.sort()
        l8.sort()
        l9.sort()
    print("------------------------------------------------------------")
    print("{} Time(s)".format(round-1))
    print("Before Radix Sort : ",end="")
    print(lloriginal.result())
    print("After  Radix Sort : ",end="")
    print(l0.result())
