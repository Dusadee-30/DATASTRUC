from itertools import permutations

print("*** Fun with permute ***")
num = []
x = [int(x) for x in input("input : ").split(',')]
for i in range(0, len(x)):
    x[i] = int(x[i])

print("Original Cofllection: " ,x)

# Get all permutations of [1, 2, 3]
perm = permutations(x)
print("Collection of distinct numbers:")
# Print the obtained permutations
for i in list(perm):
    print(i)
    for j in range(0,len(i)):
        print(i[j])
 


print("*** Fun with permute ***")
numlist = [int(x) for x in input("input : ").split(',')]

print("Original Cofllection: " ,str(numlist))

collec_nums = [[]]
for n in numlist:
    new_nums = []
    for i in collec_nums:
        for j in range(len(i)+1):
            new_nums.append(i[:j]+[n]+i[j:])
            collec_nums = new_nums
print("Collection of distinct numbers:\n",collec_nums)

