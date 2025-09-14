# HackerRank Mars Explration problem
def marsExploration(s):
    count=0
    for c in s:
        if(c=='s' or c=='o' or c=='O' or c=='S'):
            continue
        count+=1
    return count

"""This initially passed the basic test cases as it only checks whether the characters are only s or o but on submitting code it also needs checking on position so
Needs updating so here it is"""

def marsExploration(s):
    count=0
    for i,c in enumerate(s):
        if(i%3==0 and (c=='s' or c=='S')):
            continue
        elif(i%3==1 and (c=='o' or c=='O')):
            continue
        elif(i%3==2 and (c=='s' or c=='S')):
            continue
        count+=1
    return count
