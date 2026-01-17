class MyCircularQueue:
    # front and rest
    # probnlem how to check the queue is full or empty
    # if front == reat -> the queue is empty
    # if the (rear + 1) % k + 1 = front -> the queue is full

    def __init__(self, k: int):
        self.size = k + 1
        self.queue = [-1 for _ in range(self.size)]
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.front = (self.front + 1) % self.size

        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        first_element_idx = (self.front + 1) % self.size
        return self.queue[first_element_idx]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.queue[self.rear]
        
    def isEmpty(self) -> bool:
        return self.front == self.rear
        
    def isFull(self) -> bool:
        return ((self.rear + 1) % self.size) == self.front
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()