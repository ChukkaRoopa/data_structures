# Input: welcome2ourcountry34
# Output: True

# Input: stringwithoutnum
# Output: False

str = 'stringwithoutnum'
has_alphabet = False
has_digit = False
for i in str:
    if i.isalpha():
        has_alphabet = True
    if i.isdigit():
        has_digit = True
if has_alphabet and has_digit:
    print("Has one letter and aplhabet")
else:
    print("Does not have 1 letter and alphabet")    