def sub_string(s):
    res = []
    for i in range(len(s)):
        for j in range(i, len(s)):
            substr = s[i:j+1]
            if substr not in res:
                res.append(substr)
    return res
print(sub_string('Roopa'))