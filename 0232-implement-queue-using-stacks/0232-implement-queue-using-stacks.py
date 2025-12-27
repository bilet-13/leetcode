class MyQueue:

    def __init__(self):
        self.push_queue = []
        self.pop_queue = []

    def _fill_pop_queue_with_push_queue(self):
        while self.push_queue:
            x = self.push_queue.pop()
            self.pop_queue.append(x)

    def push(self, x: int) -> None:
        self.push_queue.append(x)

    def pop(self) -> int:
        if not self.pop_queue:
            self._fill_pop_queue_with_push_queue()

        result = self.pop_queue.pop()
        return result

    def peek(self) -> int:
        if not self.pop_queue:
            self._fill_pop_queue_with_push_queue()
        
        return self.pop_queue[-1] 

    def empty(self) -> bool:
        return not self.pop_queue and not self.push_queue
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()