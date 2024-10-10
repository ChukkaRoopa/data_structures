# Input : test_str = ‘geeksforgeeks 33 best’ 
# Output : 19 
# Explanation : Total characters are 19 excluding spaces. 

str = 'geeksforgeeks 33 best'
count = 0
i = 0
while i < len(str):
    if str[i] != ' ':
        count += 1
    i += 1
print(count)