# It is an improved version of binary search, especially suitable for large and uniformly distributed arrays
# pos = lo + ((target - arr[lo]) * (hi - lo)) /  (arr[hi] - arr[lo])
# Time Complexity: O(log2(log2 n)) for the average case, and O(n) for the worst case
# Auxiliary Space: O(1)

def interpolation(arr, X):
    low = 0
    high = len(arr) - 1

    while low <= high and X >= arr[low] and X <= arr[high]:
        pos = low + ((high - low) // (arr[high] - arr[low])) * (X - arr[low])

        if arr[pos] == X:
            print("Element is present at index: ", pos) 
            return
        elif X < arr[pos]:
            high = pos - 1
        else:
            low = pos + 1
    
    print("Element is not present")

arr = [11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
X = 23
interpolation(arr, X)