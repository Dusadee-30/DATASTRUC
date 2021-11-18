def maxIndex( a , index , n ):
    if index == n:
        return index 
    k = maxIndex(a, index + 1, n)   
    return (index if int(a[index]) < int(a[k]) else k)
 
def sort(lst, n, index = 0):
 
    if index == n:
        return -1    
    k = maxIndex(lst, index, n-1)  
    if k != index:
        lst[k], lst[index] = int(lst[index]), int(lst[k])
    else:
        lst[index] = int(lst[index])  
    sort(lst, n, index + 1)

Input_lst = input('Enter Input : ').split(' ')
sort(Input_lst,len(Input_lst))
print(Input_lst)