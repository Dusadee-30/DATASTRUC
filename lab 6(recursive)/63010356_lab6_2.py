def sort(lst, n):
	if n <= 1 :
		return
	sort(lst, n - 1)

	last = lst[n - 1] 
	temp = n - 2 
	
	while (temp >= 0 and lst[temp] < last):
		lst[temp + 1] = lst[temp]
		temp = temp - 1

	lst[temp + 1] = last 


l = [int(x) for x in input("Enter your List : ").split(",")]


sort(l, len(l))
print("List after Sorted :",l)