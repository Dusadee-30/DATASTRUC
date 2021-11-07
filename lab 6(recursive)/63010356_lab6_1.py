def Min(n,lst):
    k = 0
    if n == 0:
        return 0
    elif n == 1:
        return int(lst[0])
    else:
        temp = Min(n-1,l)
        if temp < l[n-1]:
            k = temp
        else:
            k = l[n-1]
        return k
            
l = [int(x) for x in input("Enter Input : ").split()]
print("Min :",Min(len(l),l))