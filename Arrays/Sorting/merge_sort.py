'''
Merge sort is a sorting algorithm that follows the divide-and-conquer approach. It works by recursively dividing the input array 
into smaller subarrays and sorting those subarrays then merging them back together to obtain the sorted array.
          2 6 5 1            7 4 3
        2 6     5 1        7 4     3
       2  6    5   1      7   4     
       2  6    1   5      4   7
         1 2 5 6           3 4 7
              1 2 3 4 5 6 7
Time complexity = O(nlog₂n)
'''

def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # recurssion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge
        i = 0  # left_arr index
        j = 0  # right_arr index
        k = 0 # merged array index
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                k += 1
            else:
                arr[k] = right_arr[j]
                j += 1
                k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

arr = [2, 6, 5, 1, 7, 4, 3]
merge_sort(arr)
print(arr)