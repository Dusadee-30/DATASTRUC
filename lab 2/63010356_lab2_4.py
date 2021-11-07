def hbd(age):
    i = 2
    
    while True:
        agenew = 0
        age_loop = age
        j = 0
        while True:
            agenew = agenew+(age_loop % i) * (10 ** j)
            age_loop = int(age_loop / i)
            j = j+1
            if age_loop == 0:
                break
        if agenew == 20 or agenew == 21:
            break
        i = i+1

    return f'saimai is just {agenew}, in base {i}!'

year = input("Enter year : ")
print(hbd(int(year)))