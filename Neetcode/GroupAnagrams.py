def GroupAnagrams(strs):
    # s is List of strings ["act","pots","tops","cat"]
    # Group the s like [["act","cat"],["pots","tops"]]
    res = defaultdict(list)
    # A default dictionary in which values and list
    for s in strs:
        count = [0]*26
        # We have the key as list now, look like [0,0,0,..,0]
        for c in s:
            count[ord(c)-ord('a')]+=1
            # Changed the value of count accordingly
        res[tuple(count)].append(s)
    return list(res.values())
