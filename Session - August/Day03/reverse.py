"""

ip: hello, how is your 'family' guys?!

op: syugy, lim af ruoy 'siwoho' lleh?!

"""
def modify_string(input_string):
    modified_string = ""
    i = len(input_string) - 1
    
    for char in input_string:
        if char.isalpha():
            while not input_string[i].isalpha():
                i -= 1
            modified_string += input_string[i]
            i -= 1
        else:
            modified_string += char
    
    return modified_string


ip = "hello, how is your 'family' guys?!"  
op = modify_string(ip)
print("Output:", op)

