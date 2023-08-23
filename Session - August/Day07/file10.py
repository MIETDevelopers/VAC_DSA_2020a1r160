#A program to convert a simple expression to prefix
inp_expression = input("Enter an expression:")
stack = []
for i in inp_expression[::-1]:
    if i.isalnum():
        print(i,end="")
    elif i==")":
        stack.append(i)
    elif i=="(":
        while stack[-1]!=")":
            print(stack.pop(),end="")
        stack.pop()
    else:
        while len(stack)!=0 and stack[-1]!=")" and (i=="^" or i=="*" or i=="/" or i=="+" or i=="-"):
            print(stack.pop(),end="")
        stack.append(i)
while len(stack)!=0:
    print(stack.pop(),end="")