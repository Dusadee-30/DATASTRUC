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
    
q_me_output = []
q_love_output = []
q_me_output_2 =[]
q_love_output_2 = []
q_me = Queue()
q_me_place = Queue()
q_love = Queue()
q_love_place = Queue()
lst_output = []
lst_love = []
score = 0
lst = input("Enter Input : ").split(",")
for e in lst:
    lst_output.append([i for i in e.split(" ")])
for e in lst_output:
    q_me_output.append(e[0])
    q_love_output.append(e[1])
print("My   Queue =",', '.join(q_me_output))
print("Your Queue =",', '.join(q_love_output))
dict_act ={'0':'Eat','1':'Game','2':'Learn','3':'Movie'}
dict_place ={'0':'Res.','1':'ClassR.','2':'SuperM.','3':'Home'}
for e in lst_output:
    first = dict_act[e[0][0]]
    second = dict_place[e[0][2]]
    word = first+':'+second
    q_me_output_2.append(word)

    first_2 = dict_act[e[1][0]]
    second_2 = dict_place[e[1][2]]
    word_2 = first_2+':'+second_2
    q_love_output_2.append(word_2)
print("My   Activity:Location =",', '.join(q_me_output_2))
print("Your Activity:Location =",', '.join(q_love_output_2))

for i in range(len(lst)):    
    q_me.enQueue(lst[i][0])
    q_me_place.enQueue(lst[i][2])
    q_love.enQueue(lst[i][4])
    q_love_place.enQueue(lst[i][6])
#print("q_me--------",q_me.items)
#print("q_me_place--",q_me_place.items)
#print("q_love------",q_love.items)
#print("q_love_place",q_love_place.items)
#print("My   Activity:Location =",q_me.items)
  
for i in range(len(lst)):
    act_me = q_me.deQueue()
    act_love = q_love.deQueue()
    place_me = q_me_place.deQueue()
    place_love = q_love_place.deQueue()
    if act_me == act_love and place_love != place_me:
        score = score+1        
    elif act_me == act_love and place_love == place_me:
        score = score+4
    elif place_love == place_me and act_me != act_love: 
        score = score+2
    else:
        score = score-5
if score >= 7:
    print("Yes! You're my love! : Score is",str(score)+'.')
if score < 7 and score > 0:
    print("Umm.. It's complicated relationship! : Score is",str(score)+'.')
if score <=0:
    print("No! We're just friends. : Score is",str(score)+'.')
