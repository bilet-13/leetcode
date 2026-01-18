class LFUCache:
     # hash map of double linked list?
    # key = the frequency val: double linked list

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.min_freq = 0
        self.freqs = {} # key: key val: frequency
        self.elements = {} # key: key val: value
        self.cache = {} # key: frequencye order: value: dict (key:key value:value)
    
    def _update(self, key):
        freq = self.freqs[key]

        del self.cache[freq][key]

        if not self.cache[freq]:
            del self.cache[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        
        self.freqs[key] += 1
        updated_freq = self.freqs[key]

        if updated_freq not in self.cache:
            self.cache[updated_freq] = OrderedDict()

        self.cache[updated_freq][key] = None

    def get(self, key: int) -> int:
        if key not in self.elements:
            return -1

        self._update(key)
        return self.elements[key]

    def put(self, key: int, value: int) -> None:
        if key in self.elements:
            self.elements[key] = value
            self._update(key)
        
        else:
            if len(self.elements) >= self.capacity:
                pop_key, _ = self.cache[self.min_freq].popitem(last=False)
                if not self.cache[self.min_freq]:
                    del self.cache[self.min_freq]
                
                del self.elements[pop_key]
                del self.freqs[pop_key]

            self.elements[key] = value
            self.freqs[key] = 1
            self.min_freq = 1
            
            if self.freqs[key] not in self.cache:
                self.cache[self.freqs[key]] = OrderedDict()
            
            self.cache[self.freqs[key]][key] = None



        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)