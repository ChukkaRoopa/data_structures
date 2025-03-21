def prefix_sum(arr):
    
    n = len(arr)
    prefix_array = [0] * n
    prefix_array[0] = arr[0]

    for i in range(1, n):
        prefix_array[i] = prefix_array[i-1] + arr[i]

    return prefix_array

print(prefix_sum([10, 20, 10, 5, 15]))

# Time complexity - O(n)
# Space complexity - O(n) - create prfix_array of size n