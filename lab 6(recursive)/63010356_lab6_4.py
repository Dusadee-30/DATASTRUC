def pantip(k, n, arr, path):
    temp = 0
    if n == len(arr):
        if k == sum(path):
            print(' '.join(list(map(str,path))))
            return 1
        return 0
    temp += pantip(k,n+1,arr,path+[arr[n]]) 
    temp += pantip(k,n+1,arr,path) 
    return temp

inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
pattern = pantip(int(inp[0]), 0, arr, [])
print("Krisada can purchase Product:",arr,"with:",inp[0],"Baht |",pattern,"Pattern")