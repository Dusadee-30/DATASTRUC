def asteroid_collision(asts):
    if len(asts) == 1:
        return asts
    res = asteroid_collision(asts[1:])

    if len(res) > 0 and asts[0] > 0 and res[0] < 0:
        if asts[0] == abs(res[0]): 
            if len(res) > 1:
                return res[1:]  
            elif len(res) == 1:
                return []  
        elif asts[0] > abs(res[0]):  
            return asteroid_collision([asts[0]] + res[1:])
        elif asts[0] < abs(res[0]):  
            return res  
    else:       
        return [asts[0]] + res 

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x))