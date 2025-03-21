# Two sum
def two_sum_array(arr, target):

    arr.sort()

    low = 0
    high = len(arr) - 1

    while low < high:
        sum = arr[low] + arr[high]

        if sum == target:
            return True
        elif sum < target:
            low += 1
        else:
            high -= 1
    return False

print(two_sum_array([0, -1, 2, -3, 1], -2))

# To return the index of the result
def two_sum_array(arr, target):
    
    indexed_array = [(num, i) for i, num in enumerate(arr)]
    indexed_array.sort()

    low = 0
    high = len(arr) - 1

    while low < high:
        sum = indexed_array[low][0] + indexed_array[high][0]

        if sum == target:
            return [indexed_array[low][1], indexed_array[high][1]]
        elif sum < target:
            low += 1
        else:
            high -= 1
    return "Elements not found"

print(two_sum_array([0, -1, 2, -3, 1], -2))

# Time complexity - O(n) - either increase left or decrease right or stop the loop
# Space complexity - O(1)