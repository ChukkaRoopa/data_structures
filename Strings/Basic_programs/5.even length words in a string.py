# Input: s = "This is a python language"
# Output: This is python language

s = "This is a python language"
lst = s.split()
print(lst)
words = []

for i in lst:
    count = 0
    for j in i:
        count += 1
    
    if count % 2 == 0:
        words.append(i)

res = ' '.join(words)
print(res)