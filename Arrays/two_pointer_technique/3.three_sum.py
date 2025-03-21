# Highest sum of subarray of length 3 

def three_sum(arr):

    target = 0
    res = []
    
    for i in range(len(arr)-2):
        sub_arr = arr[i:i+3]
        sub_array_sum = sum(sub_arr)

        if sub_array_sum > target:
            target = sub_array_sum
            res = sub_arr

    return res, target

print(three_sum([5,9,1,8,7]))