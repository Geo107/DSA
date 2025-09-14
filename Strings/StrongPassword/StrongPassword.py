def StrongPassword(n,password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    has_number=any(c in numbers for c in password)
    has_lowerCase=any(c in lower_case for c in password)
    has_upperCase=any(c in upper_case for c in password)
    has_specialCharacters=any(c in special_characters for c in password)

    missing_type=0
    if not has_number:
        missing_type+=1
    if not has_lowerCase:
        missing_type+=1
    if not has_upperCase:
        missing_type+=1
    if not has_specialCharacters:
        missing_type+=1

    return max(missing_type,6-n)
