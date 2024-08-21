'''
Binary Search Algorithm is a searching algorithm used in a sorted array by repeatedly dividing the search interval in half. The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(log N)
Time complexity = O(log N)
'''

# Here we use a while loop to continue the process of comparing the key and splitting the search space in two halves.

def binarySearch(arr, X):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == X:
            return mid
        elif arr[mid] < X:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = [2, 5, 25 , 35, 67, 89]
X = 67
result = binarySearch(arr, X)
if result == -1:
    print("element not found!!")
else:
    print("element is at index: ", result)