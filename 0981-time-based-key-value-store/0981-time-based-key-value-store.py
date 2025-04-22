class TimeMap:

    def __init__(self):
        self._history_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._history_map[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self._history_map:
            return ""
        
        history = self._history_map[key]
        result = ""

        left = 0
        right = len(history) - 1

        while left <= right:
            mid = (left + right) // 2

            if history[mid][0] > timestamp:
                right = mid - 1
            else:
                result = history[mid][1]
                left = mid + 1
        return result
