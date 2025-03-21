# problem1 - you are given an array , you should find the max length of subarray which has atmost k ones
# example - [0,1,3,1,1,6,7,1,0,1] , k = 2 - output - 5

def problem1(arr):

    n = len(arr)
    l = 0
    k = 2

    # temp to store the 1's count 
    temp = 0

    # to store valid arrays
    ans = []
    final_result = 0

    for r in range(n):

        ans.append(arr[r])

        if arr[r] == 1:
            temp += 1

        while temp > k:
            if ans[0] == 1:
                temp -= 1
            ans.pop(0)
            l += 1

        final_result = max(final_result, len(ans))

    return final_result
           
print(problem1([0,1,3,1,1,6,7,1,0,1]))

# another way
def problem1(arr):

    n = len(arr)
    l = 0
    k = 2

    # temp to store the 1's count 
    temp = 0

    # to store valid arrays
    ans = 0

    for r in range(n):

        if arr[r] == 1:
            temp += 1

        while temp > k:
            if arr[l] == 1:
                temp -= 1
            l += 1

        ans = max(ans, r-l+1)

    return ans
           
print(problem1([0,1,3,1,1,6,7,1,0,1]))