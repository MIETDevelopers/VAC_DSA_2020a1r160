#Sorting of stack
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
            return self.items[-1]

    def size(self):
        return len(self.items)

    def sort_stack(self):
        temp_stack = Stack()
        while not self.is_empty():
            temp = self.pop()
            while not temp_stack.is_empty() and temp_stack.peek() < temp:
                self.push(temp_stack.pop())
            temp_stack.push(temp)
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

stack = Stack()
stack.push(8)
stack.push(4)
stack.push(9)
stack.push(11)
print("Original stack:", stack.items)
stack.sort_stack()
print("Sorted stack:", stack.items)