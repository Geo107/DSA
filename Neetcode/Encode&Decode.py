def Encode(strs):
    s = ""
    for c in strs:
        s+=str(len(c))+"#"+c
    return s
# ["Leet","Code"] => 4#Leet4#Code
def Decode(s):
    res = []
    i=0
    while i<len(s):
        j=i
        while s[j]!="#":
            j+=1
        length = int(s[i:j])
        #length = 4
        word = s[j+1:j+1+length]
        #word=Leet
        res.append(word)
        i=j+1+length
    return res
