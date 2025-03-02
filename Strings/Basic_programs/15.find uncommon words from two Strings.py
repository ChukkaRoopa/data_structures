# Input : A = “Geeks for Geeks”,  B = “Learning from Geeks for Geeks”
# Output : [‘Learning’, ‘from’]


# Input : A = “apple banana mango” , B = “banana fruits mango”
# Output : [‘apple’, ‘fruits’]

str1 = "Geeks for Geeks"
str2 = "Learning from Geeks for Geeks"

output = []
lst1 = str1.split()
lst2 = str2.split()

for i in lst2:
    if i not in lst1:
        output.append(i)
print(output)