'''
A String is a data structure in Python Programming that represents a sequence of characters. Strings in Python can be created 
using single quotes or double quotes or even triple quotes. 
'''

# Accessing characters in string

# Positive indexing 
string = "software Engineer Trainee"
print("Positive indexing: ", string[0])

# Negative indexing
print("Negative indexing: ", string[-9])

# Slicing 
print("Slicing from 3 to end character: ", string[3:])
print("Slicing from 4 to last 3rd charater: ", string[4:-3])

# String reverse
rev_str = string[::-1]
print("Reverse string: ", rev_str)

# Buildin reverse function
rev_str1 = "".join(reversed(string))
print("Reverse of string using buildIn function: ", rev_str1)

# Python strings are immutable - they doesnot support item updation directly
# Updating a character
# Method 1

list1 = list(string)
list1[2] = 'r'
string = ''.join(list1)
print("Updating second char: ", string)

# Method 2
string = string[0:2] + 'r' + string[3:]
print("Updating char at second position: ", string)

# Update entire string
string = "Cisco Systems Private Ltd"
print("Updating entire string: ", string)

# Deleting a character
string = string[0:2] + string[3:]
print("Delete 2nd char: ", string)

# Escaping sequencing

# Escaping single quotes
string = 'I\'m a "Geek"'
print("Escaping single quotes: ", string)

# Escaping double quotes
string = "I'm a \"Geek\""
print("Escaping double quotes: ", string)

# use of tab
string = "Hi\tRoopa"
print("Use of tab: ", string)

# Use of new line
string = "Hi\nRoopa"
print("Use of new line: ", string)

''' To ignore the escape sequences in a String, r or R is used, this implies that the string is a raw string and escape sequences
inside it are to be ignored.
'''
# Printing in HEX with the use of Escape Sequences
String = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print(String)

# Printing Raw String in HEX Format (ignore escape sequences)
String = R"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print(String)

# String formatting

# Default formatting
string = "{} {} {}".format("I", "Love", "You")
print("Default formatting: ", string)

# Positional formatting
string = "{1} {2} {0}".format("I", "Love", "You")
print("Positional formatting: ", string)

# Keyword Formatting
string = "{l} {y} {i}".format(i="I", l="Love", y="You")
print("Keyword formatting: ", string )

# Formatting
string = "{0:b}".format(10)
print("Binary representation of integers: ", string)

string = "{0:e}".format(1234.903)
print("Exponential representation is:", string)

# String alignment
string = "|{:<10}|{:^10}|{:>10}".format("Geeks", "For", "Geeks")
print("string alignment: ", string)

# loop through a string
string = "Chukka Roopa"
for i in string[:8:1]:
    print(i,end = ' ')

# iterating each character using enumerate() function
string = "Roopa Reddy"
for index, char in enumerate(string):
    print(f"Char  at index {index}: {char}")
