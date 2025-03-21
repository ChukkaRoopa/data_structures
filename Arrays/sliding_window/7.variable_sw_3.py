# maximum number of consecutive 1's or 0's in the array if you can flip at most k 0's or 1's

def prblm(arr):

    n = len(arr)
    l = 0
    cnt1 = 0
    cnt0 = 0
    ans = 0
    k = 2

    for r in range(n):
        if arr[r] == 1:
            cnt1 += 1
        else:
            cnt0 += 1
        
        while min(cnt1, cnt0) > k:
            if arr[l] == 1:
                cnt1 -= 1
            else:
                cnt0 -= 1
            l  += 1

        ans =  max(ans, r-l+1)
    return ans

print(prblm([1,1,1,0,0,0,1,1,1,1,0]))