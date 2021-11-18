def maxIndex( a , index , n ):
    if index == n:
        return index 
    k = maxIndex(a, index + 1, n)   
    return (index if int(a[index]) > int(a[k]) else k)

def selection(l):
    last = len(l)-1
    while last >=1 :
        biggest = l[0]
        biggest_i = 0
        for i in range(1,last+1):
            if l[i] > biggest:
                biggest = l[i]
                biggest_i = i
        l[last],l[biggest_i] = l[biggest_i],l[last]

Input_lst = [int(x) for x in input("Enter input : ").split()]
selection(Input_lst,len(Input_lst)-1)
print(Input_lst)