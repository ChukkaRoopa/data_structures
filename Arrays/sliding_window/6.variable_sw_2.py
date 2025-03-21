# You are given an array and you should find the maximum length of subarray which has atmost k 'odd' numbers.
# example - [12,1,3,1,1,6,7,1,8,1], k = 2, output - 4

def prblm(arr):

    n = len(arr)
    l = 0
    temp = 0
    ans = 0
    k = 2

    for r in range(n):
        
        if (arr[r] % 2) != 0:
            temp += 1

        while temp > k:
            if (arr[l] % 2) != 0:
                temp -= 1
            l += 1

        ans = max(ans, r-l+1)
    return ans

print(prblm([12,1,3,1,1,6,7,1,8,1]))