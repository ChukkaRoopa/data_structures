# Input : GeeksforGeeks
# Output : No. of vowels : 5
# Explaination: The string GeeksforGeeks contains 5 vowels in it 4 letter of 'e' and 1 'o'.

str = 'GeeksforGeeks'
vowels = 'aeiouAEIOU'
count = 0
for i in str:
    if i in vowels:
        count += 1
print(count)