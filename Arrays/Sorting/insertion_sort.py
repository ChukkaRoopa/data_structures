'''
Insertion sort is a simple sorting algorithm that works by iteratively inserting each element of an unsorted list into its correct
position in a sorted portion of the list. It is a stable sorting algorithm, meaning that elements with equal values maintain their 
relative order in the sorted output.

Time complexity = O(N²)
'''

def insertion_sort(arr):

    for i in range(1,len(arr)):
        j = i
        while arr[j-1] > arr[j] and j >0:
            arr[j-1] , arr[j] = arr[j], arr[j-1]
            j -=1

arr = [2,4,6,8,3,5,1,7]
insertion_sort(arr)
print(arr)