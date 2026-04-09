from collections import OrderedDict
class LRUCache:
    # Orderdict
    # move_to_end
    # popitem
    # time complexity o(1)

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        self.map.move_to_end(key, last=False)
        return self.map[key]

    def put(self, key: int, value: int) -> None:
        if len(self.map) == self.capacity:
            self.map.popitem()
        
        self.map[key] = value
        self.map.move_to_end(key, last=False)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)