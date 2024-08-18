class RandomizedSet:

    def __init__(self):
        self.hash_table = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.hash_table:
            return False

        self.arr.append(val)
        self.hash_table[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val in self.hash_table:
            val_index = self.hash_table[val]
            self.arr[val_index], self.arr[-1] = self.arr[-1], self.arr[val_index]

            self.hash_table[self.arr[val_index]] = val_index
            del self.hash_table[self.arr[-1]]

            self.arr.pop(-1)

            return True

        return False

    def getRandom(self) -> int:
        return self.arr[random.randint(0, len(self.arr)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()