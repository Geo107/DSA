from collections import Counter
def ValidAnagram(s,t):
    return Counter(s)==Counter(t)
# Checks both the key and Value
