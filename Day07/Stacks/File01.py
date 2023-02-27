#Stacks using python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty.")

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def peekWhole(self):
        if not self.is_empty():
            return self.items

    def size(self):
        return len(self.items)

stk = Stack()
stk.push(1)
stk.push(2)
stk.push(3)
print(stk.peekWhole())
print(stk.peek())
print(stk.pop())
print(stk.peek())
print(stk.pop())
print(stk.peek())
print(stk.size())
print(stk.pop())
print(stk.peek())