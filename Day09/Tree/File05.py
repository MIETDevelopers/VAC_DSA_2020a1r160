#Evaluate expression.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def evaluate(self):
        if self.value == '+':
            return self.left.evaluate() + self.right.evaluate()
        elif self.value == '-':
            return self.left.evaluate() - self.right.evaluate()
        elif self.value == '*':
            return self.left.evaluate() * self.right.evaluate()
        elif self.value == '/':
            return self.left.evaluate() / self.right.evaluate()
        else:
            return self.value

def evaluate_expression(expression):
    operators = Stack()
    operands = Stack()
    for char in expression:
        if char.isdigit():
            operands.push(Node(int(char)))
        elif char in ['+', '-', '*', '/']:
            operators.push(Node(char))
        elif char == '(':
            continue
        elif char == ')':
            operator = operators.pop()
            operator.right = operands.pop()
            operator.left = operands.pop()
            operands.push(operator)

    while not operators.is_empty():
        operator = operators.pop()
        operator.right = operands.pop()
        operator.left = operands.pop()
        operands.push(operator)

    return operands.pop().evaluate()

print(evaluate_expression("4+(3*5)-8/2"))