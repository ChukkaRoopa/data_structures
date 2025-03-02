# Input : geeksforgeeks
# Output : Not Accepted
# All vowels except 'a','i','u' are not present

# Input : ABeeIghiObhkUul
# Output : Accepted
# All vowels are present

def all_vowels(string):
    
    string = string.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    res = []
    for i in string:
        if i in vowels and i not in res:
            res.append(i)
    print(res)

    if sorted(res) == sorted(vowels):
        print("accepted")
    else:
        print("not accepted")


all_vowels("geeksforgeeks")
all_vowels("ABeeIghiObhkUul")