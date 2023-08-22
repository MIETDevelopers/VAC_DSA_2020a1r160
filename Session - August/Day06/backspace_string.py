def backspaceCompare(S, T):
    def build_string(s):
        stack= []
        for char in s:
            if char != '#':
                stack.append(char)
            elif stack:
                stack.pop()
        return ''.join(stack)
    
    return build_string(S) == build_string(T)


S = input("S: ")
T = input("T: ")
print(backspaceCompare(S, T)) 

