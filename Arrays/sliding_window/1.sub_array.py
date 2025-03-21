def subarray(arr):
    res = []
    for i in range(len(arr)):
        for j in  range(i, len(arr)):
            sub_arr = arr[i:j+1]
            res.append(sub_arr)
    return res

print(subarray([1,3,4]))