def alterchar(s):
    t = sorted(set(s))
    # [b,e,a,f]
    for i in range(len(t)):
        for j in range(i+1,len(t)):
            print(t[i],t[j])



s ="beafffeaffbb"
alterchar(s)
