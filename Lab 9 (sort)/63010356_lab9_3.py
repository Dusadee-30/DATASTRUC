def Metadrome(lst,index = 0):
    if index == len(lst)-1:
        return True
    if lst[index] < lst[index+1]:
        return Metadrome(lst,index+1)
    else:
        return False
        
def Plaindrome(lst,index = 0):
    if index == len(lst)-1:
        return True
    if lst[index] <= lst[index+1]:
        return Plaindrome(lst,index+1)
    else:
        return False

def Katadrome(lst,index = 0):
    if index == len(lst)-1:
        return True
    if lst[index] > lst[index+1]:
        return Katadrome(lst,index+1)
    else:
        return False
        
def Nialpdrome(lst,index = 0):
    if index == len(lst)-1:
        return True
    if lst[index] >= lst[index+1]:
        return Nialpdrome(lst,index+1)
    else:
        return False

def Repdrome(lst,index = 0):
    if index == len(lst)-1:
        return True
    if lst[index] == lst[index+1]:
        return Repdrome(lst,index+1)
    else:
        return False

def Method_sort(lst):
    if Repdrome(lst):
        return "Repdrome"
    elif Metadrome(lst):
        return "Metadrome"
    elif Plaindrome(lst):
        return "Plaindrome"
    elif Katadrome(lst):
        return "Katadrome"
    elif Nialpdrome(lst):
        return "Nialpdrome"
    else:
        return "Nondrome"

Input_lst =  list(input("Enter Input : "))
print(Method_sort(Input_lst))
