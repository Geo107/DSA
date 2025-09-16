# "acxz" reverse in "zxca" the difference in ascii of these values are equal hence funny string
def FunnyString(s):
    diff=[]
    for i in range(1,len(s)):
        val=abs(ord(s[i])-ord(s[i-1]))
        diff.append(val)
    r=s[::-1]
    rdiff=[]
    for i in range(1,len(r)):
        val=abs(ord(r[i])-ord(r[i-1]))
        rdiff.append(val)
    if(diff==rdiff):
        return "Funny"
    else:
        return "Not Funny"
s="acxz"
FunnyString(s)
