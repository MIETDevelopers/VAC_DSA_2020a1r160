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

q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.show())
print(q.dequeue())
print(q.show())