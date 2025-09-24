def alternate(s):
    max_length=0
    unique_char = list(set(s))
    #beaf
    for i in range(len(unique_char)):
        for j in range(i+1,len(unique_char)):
            char1,char2 = unique_char[i],unique_char[j]

            filtered = ''.join([c for c in s if c==char1 or c==char2])
            #beebbbbbb
            if(is_alternating(filtered)):
                max_length= max(len(filtered),max_length)

    return max_length

def is_alternating(s):
    if len(s)<=1:
        return True
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            return False
    return True
s = "abababab"
print(alternate(s))
