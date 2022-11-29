aux = ""
for i in range(len(strs[0])):
    for s in strs:
        if i== len(S) or s[i] != strs[0][i]:
            aux += strs[0][i]
return aux