# Problem Definition is check whether the string have all the alphabet in english

def Pangram(s):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    return "pangram" if all(c in s.lower() for c in alphabet)else "not pangram"
# T(n) = O(n)
