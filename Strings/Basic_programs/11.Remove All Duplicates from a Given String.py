# Input : geeksforgeeks 
# Output : geksfor

str = 'Geeksforgeeks'

res_str = ''
for i in str:
    if i not in res_str:
        res_str += i
print(res_str)