'''
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order.
This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high.
Time complexity = O(n²)
'''

def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for  j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
arr = [3,4,2,8,5,6]
res = bubblesort(arr)
print(res)