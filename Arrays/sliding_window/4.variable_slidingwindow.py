# max_length is 10

def variable_sw(nums):

    n = len(nums)
    l = 0
    temp = 0
    k = 10
    ans = 0

    for r in range(n):
        temp += nums[r]

        while temp > k:
            temp -= nums[l]
            l += 1
        
        print(nums[l:r+1], sum(nums[l:r+1]))
        ans = max(ans, r-l+1)
    print(ans)

print(variable_sw([9,3,4,8,1]))