class FreqStack:


    def __init__(self):
        self.frequency_stacks = defaultdict(list)
        self.frequencies = defaultdict(int)
        self.max_frequency = 0

    def push(self, val: int) -> None:
        self.frequencies[val] += 1

        self.frequency_stacks[self.frequencies[val]].append(val)

        self.max_frequency = max(self.max_frequency, self.frequencies[val])

    def pop(self) -> int:
        most_frequent_val = self.frequency_stacks[self.max_frequency].pop()

        self.frequencies[most_frequent_val] -= 1

        if not self.frequency_stacks[self.max_frequency]:
            self.max_frequency -= 1
        
        return most_frequent_val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()