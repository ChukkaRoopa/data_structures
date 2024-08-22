arr = [1,3,5,7,9]
    #  0,1,2,3,4
d = 2
n = len(arr)
temp = []

for i in range(d+1,n):
    temp.append(arr[i])
for i in range(d+1):
    temp.append(arr[i])
print(temp)
