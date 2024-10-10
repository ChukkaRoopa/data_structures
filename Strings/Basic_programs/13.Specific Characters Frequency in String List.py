# Input : test_list = [“geeksforgeeks is best for geeks”], chr_list = [‘e’, ‘b’, ‘g’, ‘f’] 
# Output : {‘g’: 3, ‘e’: 7, ‘b’: 1, ‘f’ : 2} 
# Explanation : Frequency of certain characters extracted. 


# Input : test_list = [“geeksforgeeks”], chr_list = [‘e’, ‘g’] 
# Output : {‘g’: 2, ‘e’: 4} 
# Explanation : Frequency of certain characters extracted.

test_list = ["geeksforgeeks is best for geeks"]
chr_list = ['e','b','g','f']

output_dict = {}
for i in test_list:
    for j in i:
        if j in chr_list:
            output_dict[j] = i.count(j)
print(output_dict)