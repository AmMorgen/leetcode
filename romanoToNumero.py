roman = {"I" : 1, "V" : 5, "X" : 10,
        "L" : 50, "C" : 100, "D":500, "M": 1000}
res = 0

for i in range(len(s)):
    if 1 +1 < len(s) and roman[s[i]] < roman[s[i+1]]:
        res -= roman[s[i]]
    else:
        res +=[s[i]]
        