class StockSpanner:

    def __init__(self):
        self.day = 0
        self.stack = [(float('inf'), self.day)] # element (price, index)

    def next(self, price: int) -> int:
        self.day += 1
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()

        span = self.day - self.stack[-1][1]

        self.stack.append((price, self.day))

        return span