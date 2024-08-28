'''
Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest) element 
from the unsorted portion of the list and moving it to the sorted portion of the list. 
Time complexity is O(N²)
'''

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
arr = [3,6,8,2,4,1]
print(selection_sort(arr))