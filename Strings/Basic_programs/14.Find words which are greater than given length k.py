# Input : str = "hello geeks for geeks is computer science portal" 
#         k = 4
# Output : hello geeks geeks computer science portal
# Explanation : The output is list of all words that are of length more than k.

str = "hello geeks for geeks is computer science portal"
k = 4

output = ''
lst = str.split()
for i in lst:
    if len(i) > 4:
        output += i + ' '
print(output)