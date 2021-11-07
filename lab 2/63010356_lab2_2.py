def weirdSubtract(n,k):
 check = 1
 checkinloop = 1
 while check <= k:
   if n%10 != 0 and checkinloop == 1:
         n = n-1
         checkinloop = 0
   if n%10 == 0 and checkinloop == 1:
         n = int(n/10)
         checkinloop = 0
   if check >= k:
         break
   check = check+1    
   checkinloop = 1
	### Enter Your Code Here ###
 return n
n,s = input("Enter num and sub : ").split()

print(weirdSubtract(int(n),int(s)))