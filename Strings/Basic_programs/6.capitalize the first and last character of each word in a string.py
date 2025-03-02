# Input: welcome to geeksforgeeks
# Output: WelcomE TO GeeksforgeekS

str = "welcome to geeksforgeeks"
words = str.split()
updated_list = []

for i in words:
    if len(i) > 1:
        updated_word = i[0].upper() + i[1:-1] + i[-1].upper()
    else:
        updated_word = i.upper()
    updated_list.append(updated_word)

res = ' '.join(updated_list)
print(res)