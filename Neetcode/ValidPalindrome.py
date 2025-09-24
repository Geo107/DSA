def ValidPalindrome(s):
    cleaned = ""
    for c in s:
        if c.isalnum():
            cleaned+=c
    return cleaned.lower()==cleaned.lower()[::-1]
