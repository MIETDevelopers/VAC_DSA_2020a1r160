#Stacks using python
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items

    def size(self):
        return len(self.items)

stk = Stack()
stk.push(1)
stk.push(2)
stk.push(3)
print(stk.peek())
print(stk.pop())
print(stk.peek())
print(stk.size())