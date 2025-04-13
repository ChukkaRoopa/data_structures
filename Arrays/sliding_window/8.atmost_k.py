# return number of subarrays with atmost k odd numbers

def atmost(nums,k):

    l = 0
    n = len(nums)
    temp = 0
    ans = 0

    for r in range(n):

        if (nums[r] % 2) != 0:
            temp += 1

        while temp > k:
            if (nums[l] % 2) != 0:
                temp -= 1
            l += 1
       
        ans += r-l+1
        print(nums[l:r+1])

    return ans
        
print(atmost([1,3,4,5,7],1))      