class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def reverse(self):
        temp_stack = Stack()
        while not self.is_empty():
            temp_stack.push(self.pop())
        print("Reversed stack: ", temp_stack.items)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print("Original stack:", stack.items)
stack.reverse()