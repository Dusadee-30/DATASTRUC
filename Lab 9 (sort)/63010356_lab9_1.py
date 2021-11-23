def bubble_sort(list):
    last = len(list)-1
    swaped = True
    while last >= 1:
        swaped = False
        i = 0
        while(i < last):
            if list[i] > list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
                swaped = True
            i+=1
        if not swaped:
            break

Input_lst = [int(i) for i in input('Enter Input : ').split(' ') ]
bubble_sort(Input_lst)
print(Input_lst)