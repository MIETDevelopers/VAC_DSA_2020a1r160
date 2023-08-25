#Program to check that input string in panagram or not
def panagram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
    return True
string = input("Enter the string: ")
if(panagram(string) == True):
    print("Yes, it is panagram")
else:
    print("No, it is not panagram")