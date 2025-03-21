''' It is easy and effective technique that is typically used for "Two sum in sorted arrays", "Closed two sum", "Three sum",
"Four sum", "Trapping rain water"
'''

''' Given a sorted array arr (sorted in ascending order) and a target, find if there exists any pair of elements (arr[i], arr[j]) 
such that their sum is equal to the target.'
'''

# Two sum

def two_sum_array(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]

print(two_sum_array([0, -1, 2, -3, 1], -2))

# Time complexity - O(n^2)
# Space complexity - O(1)