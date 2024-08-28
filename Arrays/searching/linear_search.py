def search(arr, X):
    for i in range(len(arr)):
        if arr[i] == X:
            return i
    return -1

arr = [2, 3, 45, 78 , 32]
X = 3
result = search(arr, X)
if result == -1:
    print("element not found")
else:
    print("element is at index: ", result)


'''
Linear search is a method for searching for an element in a collection of elements. In linear search, each element of the collection
is visited one by one in a sequential fashion to find the desired element. Linear search is also known as sequential search.
Time Complexity - best case = O(1)
                - worst case = O(N)
When we have an unsorted array or list, linear search is most commonly used to find any element in the collection.
'''