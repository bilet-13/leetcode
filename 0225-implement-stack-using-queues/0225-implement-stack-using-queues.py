class MyStack:

    def __init__(self):
        self.store_queue = deque()   
        self.top_queue = deque()   

    def push(self, x: int) -> None:
        # o(1)
        self.store_queue.append(x)

    def pop(self) -> int:
        # o(n)
        while len(self.store_queue) > 1:
           x = self.store_queue.popleft() 
           self.top_queue.append(x)
        
        top_x = self.store_queue[0]
        self.store_queue.popleft() 

        self.store_queue, self.top_queue = self.top_queue, self.store_queue

        return top_x
        
    def top(self) -> int:
        # o(n)
        while len(self.store_queue) > 1:
           x = self.store_queue.popleft() 
           self.top_queue.append(x)
        
        top_x = self.store_queue[0]
        x = self.store_queue.popleft() 
        self.top_queue.append(x)

        self.store_queue, self.top_queue = self.top_queue, self.store_queue

        return top_x

    def empty(self) -> bool:
        # o(1)
        return len(self.store_queue) == 0
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()