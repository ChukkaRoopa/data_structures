def fun(list1):
    element = 0
    count = 0

    for i in list1:
        current_count = list1.count(i)
        if current_count > count:
            count = current_count
            element = i
    return element

list1 = [1,3,4,2,2,3,3,6]
print(fun(list1))