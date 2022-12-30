from numberpartitioning import karmarkar_karp
numbers = [1,3,4,1,1]
result = karmarkar_karp(numbers, num_parts=5)
arr = []
res = 0
for i in result.partition:
    for  j in i:
        res+= j
    arr.append(res)
    res = 0
temp = arr[0]
flag = True
for i in arr:
    if i != temp:
        flag = False

if flag:
    print("Following are sets")
    for i in result.partition:
        print(i)
else:
    print("No Possible Sets")        
        

