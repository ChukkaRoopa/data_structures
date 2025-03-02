# Using map(), join, lsit slicing

test_list = ['gfg', 'is', 'good', 'for', 'geek', 'people']

N = 3

res = list(map(' '.join, [test_list[i:i + N] for i in range(0,len(test_list), N)]))

print(res)

# using for loop

test_list = ['gfg', 'is', 'good', 'for', 'geek', 'people']
N = 3

res = []
for i in range(0, len(test_list), N):
    out = test_list[i:i + N]
    res1 = ' '.join(out)
    res.append(res1)
print(res)

