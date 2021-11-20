def greaterThan(index, array, x):
    if index > len(array) - 1:              
        return 'No First Greater Value'

    if array[index] <= x:
        return greaterThan(index + 1, array, x)     
    elif array[index] > x:                 
        return array[index]                      


inputlst, temp = input('Enter Input : ').split('/')
inputlst = [int(i) for i in inputlst.split()]
temp = [int(i) for i in temp.split()]

inputlst.sort()    

for i in temp:
    print(greaterThan(0, inputlst, i)) 