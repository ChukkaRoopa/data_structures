# Array reverse using an extra array

def reverse_array_extra_aray(arr):
    rev_arr = arr[::-1]
    return rev_arr
arr = [1, 2, 3, 4, 5]
print(reverse_array_extra_aray(arr))


# array reverse using a loop

def reverseList(arr, start, end):
    while start < end :
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr
arr = [6,7, 8, 9, 10]
print(reverseList(arr, 0, 4))

def rev(arr):
    n  = len(arr)
    for i in range(n // 2):
        arr[i], arr[n-i-1] = arr[n-i-1] , arr[i]
    return arr
arr = [1,2,4,5,6]
print(rev(arr))

# array reverse inbuild methods

arr = [1, 2,3 ,4]
rev_arr = list(reversed(arr))
print(rev_arr)

# using stack

arr = [1,2, 3,4 , 6]
stack = []
for i in range(len(arr)):
    stack.append(arr[i])
for i in range(len(arr)):
    arr[i] = stack.pop()
print(arr)
