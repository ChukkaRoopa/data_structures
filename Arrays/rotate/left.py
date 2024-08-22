# rotate an array by d positions to the left using temp array

arr = [1,2,3,4 ,5,6,7]
d = 2
n = len(arr)
temp = []
for i in range(d,n):
    temp.append(arr[i])
for i in range(d):
    temp.append(arr[i])
for i in range(n):
    arr[i] = temp[i]
print(arr)

# rotate one by one

def rotate(arr, d):
    n = len(arr)

    for i in range(d):
        first = arr[0]
        for i in range(n-1):
            arr[i] = arr[i +1]
        arr[n-1] = first
    print(arr)

arr = [1,2,3,4,5,6,7,8,9,10]
d = 2
rotate(arr, d)

