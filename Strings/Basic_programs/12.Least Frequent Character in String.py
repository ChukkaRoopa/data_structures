str = 'GeeksforGeeks'

dict1 = {}
for i in str:
    dict1[i] = str.count(i)
print(dict1)

min_dict1 = min(dict1, key=dict1.get)
print("Min value: ",min_dict1)

max_dict1 = max(dict1, key = dict1.get)
print("Max value: ", max_dict1)

# Odd Frequency Characters

str = 'GeeksforGeeks'

dict1 = {}
odd_freq = []
for i in str:
    dict1[i] = str.count(i)

for keys, values in dict1.items():
    if values % 2 != 0:
        odd_freq.append(keys)
print(odd_freq)