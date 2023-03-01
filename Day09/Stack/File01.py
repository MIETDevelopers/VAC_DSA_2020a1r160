class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

def is_valid_expression(expression):
    stack = Stack()
    for char in expression:
        if char in ['(', '[', '{']:
            stack.push(char)
        elif char in [')', ']', '}']:
            if stack.is_empty():
                return False
            top_char = stack.pop()
            if (top_char == '(' and char != ')') or \
               (top_char == '[' and char != ']') or \
               (top_char == '{' and char != '}'):
                return False
    return stack.is_empty()

expression = str(input())
if is_valid_expression(expression):
    print("Valid")
else:
    print("Invalid")