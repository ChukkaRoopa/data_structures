lst1 = [1, 2, 3, 4]
lst2 = ['a', 'b', 'c', 'd', 'e']

res = []
min_length = min(len(lst1), len(lst2))

for i in range(min_length):
    res.append(lst1[i])
    res.append(lst2[i])

res += lst1[min_length:] + lst2[min_length:]

print(res)