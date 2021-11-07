def mod_position(arr, s):
 lst = []
 s_int = int(s)  
 count = int(s)
 s_int = s_int-1
 lst.append(arr[s_int])
 while s_int < len(arr):
     s_int = s_int+count
     if s_int >= len(arr):
         break
     lst.append(arr[s_int])

 return lst

print("*** Mod Position ***")
arr,s = input("Enter Input : ").split(",")

#mod_position(arr,s)
print(mod_position(arr,s))