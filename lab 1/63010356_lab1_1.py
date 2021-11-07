print("*** Converting hh.mm.ss to seconds ***")
h,m,s = [int(x) for x in input("Enter hh mm ss : ").split()]
time = (h*60*60)+(m*60)+s
if h < 0:
    print( "hh(%d) is invalid!" %(h))
elif m < 0 or m >= 60 :
    print( "mm(%d) is invalid!" %(m))
elif s < 0 or s >= 60 :
    print( "ss(%d) is invalid!" %(s))
else :
    print("%02d:%02d:%02d ="%(h,m,s),f"{time:,} seconds")
