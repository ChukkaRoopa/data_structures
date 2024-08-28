'''
Ternary search is a search algorithm that is used to find the position of a target value within a sorted array. It operates on 
the principle of dividing the array into three parts instead of two, as in binary search. The basic idea is to narrow down the 
search space by comparing the target value with elements at two points that divide the array into three equal parts.
mid1 = l + (r - l) // 3
mid2 = r - (r - l) // 3
The array is now effectively divided into [left, mid1], (mid1, mid2), and [mid2, right]
Time complexity = O(log₃(n))

'''

def ternarySearch(arr, key):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3

        if key == arr[mid1]:
            return mid1
        if key == arr[mid2]:
            return mid2
        
        if key < arr[mid1]:
            r = mid1 - 1
        elif key > arr[mid2]:
            l = mid2 + 1
        else:
            l = mid1 + 1
            r = mid2 - 1

    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
key = 2
result = ternarySearch(arr, key)
if result == -1:
    print("element not found")
else:
    print("Element found at index: ", result)