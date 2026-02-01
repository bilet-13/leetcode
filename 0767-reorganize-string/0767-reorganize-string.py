class Solution:
    def reorganizeString(self, s: str) -> str:
          
        freqs = Counter(s)
        max_heap = [(-freq, char) for char, freq in freqs.items()]
        heapq.heapify(max_heap)

        result = []
        n = len(s)
        
        prev = None
        prev_negative_count = 0

        while max_heap:
            negative_freq, char = heapq.heappop(max_heap)
            result.append(char)

            if prev_negative_count < 0:
                heapq.heappush(max_heap, (prev_negative_count, prev))

            prev = char
            prev_negative_count = negative_freq + 1

        if len(result) < n:
            return ""

        return "".join(result)
            