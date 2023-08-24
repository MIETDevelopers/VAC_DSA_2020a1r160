class StackNode :
    #  Stack data
    def __init__(self, element, next) :
        self.element = element
        self.next = next
    

#  Define a custom stack
class MyStack :
    def __init__(self) :
        self.top = None
        self.size = 0
    
    #  Add node at the top of stack
    def push(self, element) :
        self.top = StackNode(element, self.top)
        self.size += 1
    
    def isEmpty(self) :
        if (self.size > 0 and self.top != None) :
            return False
        else :
            return True
        
    
    #  Remove top element of stack
    def pop(self) :
        c = ""
        if (self.size > 0 and self.top != None) :
            temp = self.top
            #  Change top element of stack
            self.top = temp.next
            self.size -= 1
            c = temp.element
        
        return c
    
    #  Return top element of stack
    def peek(self) :
        if (self.top == None) :
            return ""
        
        return self.top.element
    

class Conversion :
    def precedence(self, text) :
        if (text == "+"
            or text == "-") :
            return 1
        elif (text == "*"
            or text == "/") :
            return 2
        elif (text == "^") :
            return 3
        
        return -1
    
    def isOperator(self, text) :
        if (self.precedence(text) != -1) :
            return True
        
        return False
    
    #  Converting the given infix 
    #  expression to prefix expression
    def infixToPrefix(self, infix) :
        #  Get the size
        size = len(infix)
        #  Create stack object
        s = MyStack()
        op = MyStack()
        #  Some useful variables which is using of to 
        #  storing current result
        auxiliary = ""
        op1 = ""
        op2 = ""
        isValid = True
        i = 0
        while (i < size and isValid) :
            if (infix[i] == '(') :
                op.push("(")
            elif (self.isOperator(str(infix[i])) == True) :
                #  When get a operator 
                while (s.size > 1 and self.precedence(
                       str(infix[i])) <= self.precedence(op.peek())) :
                    op1 = s.pop()
                    op2 = s.pop()
                    auxiliary = op.pop() + op2 + op1
                    #  Add new result into stack
                    s.push(auxiliary)
                
                auxiliary = str(infix[i])
                op.push(auxiliary)
            elif (infix[i] == ')') :
                if (s.size > 1) :
                    while (s.size > 1 and not op.peek() == "(") :
                        op1 = s.pop()
                        op2 = s.pop()
                        auxiliary = op.pop() + op2 + op1
                        #  Add new result into stack
                        s.push(auxiliary)
                    
                    op.pop()
                else :
                    isValid = False
                
            elif ((infix[i] >= '0'
                    and infix[i] <= '9') or(infix[i] >= 'a'
                    and infix[i] <= 'z') or(infix[i] >= 'A'
                    and infix[i] <= 'Z')) :
                auxiliary = str(infix[i])
                s.push(auxiliary)
            else :
                isValid = False
            
            i += 1
        
        if (isValid == False) :
            print("Invalid infix : ", infix, end = "")
        else :
            #  Display result
            print(" Infix   : ", infix)
            print(" Prefix  : ", s.pop())
        
    

def main() :
    task = Conversion()
    #  Test
    infix = "((a*b)+(c^d))"
    task.infixToPrefix(infix)
    infix = "((a/(b-c+d))*(e-a)*c)"
    task.infixToPrefix(infix)

if __name__ == "__main__": main()