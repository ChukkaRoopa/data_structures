# Highest sum of subarray of length 3 using sliding window

def threesum(arr):

    n = len(arr)
    l = 0
    temp = 0 
    ans = 0
    max_array_index = 0

    for r in range(n):
        temp += arr[r]

        if (r-l == 3):
            temp -= arr[l]
            l += 1
        
        if (r - l + 1 == 3):
            if temp > ans:
                ans = temp
                max_array_index = l
            
    return ans, (max_array_index, max_array_index+3), arr[max_array_index:max_array_index+3]

print(threesum([5,9,1,8,7]))