string = "RooPa ChUKka"

print(string.lower())
print(string.upper())
print(string.swapcase())
print(string.title())
print(string.capitalize())

# count
print("count: ", string.count('o'))

# encoding

# Feature	                 ASCII	                                  UTF-8
# Character Range	    128 characters	                         Over 1.1 million
# Byte Size	               1 byte	                               1 to 4 bytes
# Language Support	    English only	                           Multilingual
# Compatibility	       Not backward-compatible with UTF-8	  Backward-compatible with ASCII

print("encode of ¶ using utf-8: ", '¶'.encode('utf-8'))

# print("encode using ascii: " , '¶'.encode('ascii')) # throws error

# using "errors" parameters  to ignore errors while encoding
print("encode using ascii: " , '¶'.encode('ascii', errors='ignore'))

# endswith()
text = "geeks for geeks."
print(text.endswith("geeks."))
print(text.endswith("geeks", 10, 16))
print(text.endswith("geeks", 10, 15))

# find()
print("find() method")
print(text.find("for"))
print(text.find("s",3,20))
print(text.find("geeks ",4,30))

# replace()
print(text.replace("geeks","code"))

# index()
print("index() method")

print(text.index("for",30))
