#Password Problem
def is_strong_password(password):
    if len(password) < 6:
        return False

    has_uppercase = False
    has_digit = False
    has_special_char = False
    special_chars_count = 0
    
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_digit = True
        elif char in "!@#$%^&*()_+-={}[]|\:;\"'<>,.?/":
            has_special_char = True
            special_chars_count += 1
        
    if not has_uppercase or not has_digit or not has_special_char or special_chars_count < 2:
        return False
    
    if len(set(password)) != len(password):
        return False
    
    return True

password = str(input())
print(is_strong_password(password))