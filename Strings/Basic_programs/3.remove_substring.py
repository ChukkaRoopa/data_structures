# Input: 'Geeks123For123Geeks'
# Output: GeeksForGeeks
# Explanation: In This, we have removed the '123' character from a string.

string = 'Geeks123For123Geeks'
removal_str = '123'
res = ''

i = 0
while i < len(string):
    if string[i:i+len(removal_str)] == removal_str:
        i += len(removal_str) 
    else:
        res += string[i]
        i += 1
print(res)

# remove a single character 
string = 'Geeks for geeks'
char_to_remove = 'e'
res = ''
for i in string:
    if i != char_to_remove:
        res += i
print(res)