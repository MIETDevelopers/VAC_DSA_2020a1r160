import re

def is_strong_password(password):
    if len(password) < 6:
        return False
    
    if not re.search(r'[A-Z]', password):
        return False
    
    if not re.search(r'\d', password):
        return False
    
    if not re.search(r'[!@#$%^&*()_+{}|:"<>?`\-=\[\]\\;\',./]', password):
        return False
    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            return False
    return True

password = str(input())
print(is_strong_password(password))