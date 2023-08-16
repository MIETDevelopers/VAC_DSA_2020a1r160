#Circular Queue
class CircularQueue:
    def __init__(self, k: int):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    def is_empty(self) -> bool:
        return self.head == -1

    def is_full(self) -> bool:
        return (self.tail + 1) % self.k == self.head

    def enqueue(self, data: int) -> bool:
        if self.is_full():
            return False
        elif self.is_empty():
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data
        return True

    def dequeue(self) -> int:
        if self.is_empty():
            return -1
        elif self.head == self.tail:
            data = self.queue[self.head]
            self.head = -1
            self.tail = -1
        else:
            data = self.queue[self.head]
            self.head = (self.head + 1) % self.k
        return data

    def display(self) -> None:
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Circular Queue:")
            if self.tail >= self.head:
                for i in range(self.head, self.tail + 1):
                    print(self.queue[i], end=" ")
            else:
                for i in range(self.head, self.k):
                    print(self.queue[i], end=" ")
                for i in range(0, self.tail + 1):
                    print(self.queue[i], end=" ")
            print()

cq = CircularQueue(5)

cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.display()
cq.enqueue(5)
cq.display()
cq.dequeue()
cq.dequeue()
cq.display()
cq.enqueue(6)
cq.enqueue(7)
cq.display()
cq.dequeue()
cq.display()
cq.enqueue(8)
cq.enqueue(9)
cq.display()