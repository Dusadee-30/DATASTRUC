def pow(a,b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        b -= 1
        return pow(a,b)*a
    
a,b = [int(x) for x in input("Enter Input a b : ").split(" ")]
print(pow(a,b))