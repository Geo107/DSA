# HACKERANK CAMELCASE PROBLEM

def CamelCase(s):
    c=1
    for i in s:
        if(s.isupper()):
            c+=1
    return c

# Why c initialized to 1 because the checking goes like whenever a character is uppercase count is incremented so the first word is all LOWERCASE hence c=1
