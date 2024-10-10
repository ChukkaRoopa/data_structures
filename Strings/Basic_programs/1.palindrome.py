# Method 1 - using loop
 
def palindrome1(string):
    rev_str = ""
    for i in string:
        rev_str = i + rev_str
    if string == rev_str:
        return True
    return False
print(palindrome1("madam"))
print(palindrome1("madamasdf"))

# method 2 - using slicing
# To check the string is symmetrical and palindrome
# string is symmetrical if both halves are same

def palindrome2(string):
    return string == string[::-1]

def symmetrical(string):
    length = len(string)
    mid = length // 2

    if length % 2 == 0:
        return string[:mid] == string[mid:]
    else:
        return string[:mid] == string[mid+1:]
    
string = "khokho"
if palindrome2(string):
    print("String is palindrome")
else:
    print("string is not palindrome")

if symmetrical(string):
    print("String is symmerical")
else:
    print("String is not symmetrical")