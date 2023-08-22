def backspaceCompare(S, T):
    def build_string(s):
        lis= []
        for char in s:
            if char != '#':
                lis.append(char)
            elif lis:
                lis.pop()
        return ''.join(stack)
    
    return build_string(S) == build_string(T)


S = input("S: ")
T = input("T: ")
print(backspaceCompare(S, T)) 

