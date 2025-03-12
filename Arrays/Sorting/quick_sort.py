'''
QuickSort is a sorting algorithm based on the Divide and Conquer algorithm that picks an element as a pivot and partitions the given
array around the picked pivot by placing the pivot in its correct position in the sorted array.

'''

def partition(arr, low, high):

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i] , arr[j] = arr[j], arr[i]

    arr[i+1] , arr[high] = arr[high] , arr[i+1]
    return i + 1

def quicksort(arr):
    stack = [(0, len(arr)-1)]

    while stack:
        low, high = stack.pop()

        if low < high:
            partition_index = partition(arr, low, high)

            if partition_index - 1 > low:
                stack.append((low, partition_index - 1))

            if partition_index + 1 < high:
                stack.append((partition_index + 1, high))

    return arr

arr = [10,80,30,90,40]
print(quicksort(arr))