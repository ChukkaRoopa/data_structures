# reverse words in the given string
# Input : str = "geeks quiz practice code"
# Output : str = code practice quiz geeks 

# method 1
str = "geeks quiz practice code"
for i in str:
    string = str.split()
    res = ' '.join(string[::-1])
print(res)

# method 2 - without build - in functions

str1 = "geeks quiz practice code"
words = []
word = ''

for i in str1:
    if i == " ":
        words.append(word)
        word = ''
    else:
        word += i
words.append(word)
print(words)

# reverse the list 
rev_list = []
for i in range(len(words)-1,-1,-1):
    rev_list.append(words[i])

print(rev_list)

# convert back into string
res = ''
for i in range(len(rev_list)):
    res = res + rev_list[i] + ' '

print(res)