# linear data structure which stores objects in FIFO format. the least recently added element is removed first.
# In a queue, we have two things --- Front and Rare
# Adding an element is called Enqueue
# Deleting an element is called Dequeue
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items.pop(0)

    def size(self):
        return len(self.items)
    
    def show(self):
        if not self.is_empty():
            return self.items
    
    def front(self):
        return self.items[-1] 
    
    def rear(self):
        return self.items[0]

    def reverse(self):
        stack = []
        while not self.is_empty():
            stack.append(self.dequeue())
        while stack:
            self.enqueue(stack.pop())
    
    def sort(self):
        temp_queue = Queue()

        while not self.is_empty():
            # find smallest element in queue
            smallest = self.items[0]
            for item in self.items:
                if item < smallest:
                    smallest = item

            self.items.remove(smallest)
            temp_queue.enqueue(smallest)

        while not temp_queue.is_empty():
            self.enqueue(temp_queue.dequeue())

        return self.items

q = Queue()

q.enqueue(69)
q.enqueue(40)
q.enqueue(99)
print(q.show())
print(q.sort())