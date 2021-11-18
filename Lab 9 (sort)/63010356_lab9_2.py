def maxIndex( a , index , n ):
    if index == n:
        return index 
    k = maxIndex(a, index + 1, n)   
    return (index if int(a[index]) > int(a[k]) else k)

def selection(lst,last,index = 0):
    index = 0
    if last == 0:
        return -1
    biggest = lst[0]
    biggest_i = 0
    I = maxIndex(lst , index ,last)
    if lst[I] > biggest:
        biggest = lst[I]
        biggest_i = I
    temp1 = lst[last]
    temp2 = lst[biggest_i]
    if lst[last] != lst[biggest_i]:
        lst[last],lst[biggest_i] = lst[biggest_i],lst[last]
        print('swap {a} <-> {b} :'.format(a = temp1,b = temp2),lst)
    selection(lst,last-1,index+1)

Input_lst = [int(x) for x in input("Enter Input : ").split()]
selection(Input_lst,len(Input_lst)-1)
print(Input_lst)