class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = [(-freq, char) for freq, char in [(a, 'a'), (b, 'b'), (c, 'c')] if freq != 0]
        heapq.heapify(max_heap)
        result = []

        while max_heap:
            top_freq, top_char = heapq.heappop(max_heap)
    
            if len(result) >= 2 and result[-2] == result[-1] and result[-1] == top_char:
                if not max_heap:
                    break
    
                second_freq, second_char = heapq.heappop(max_heap)
                result.append(second_char)
    
                second_freq += 1
                if second_freq != 0:
                    heapq.heappush(max_heap, (second_freq, second_char))
                
                heapq.heappush(max_heap, (top_freq, top_char))
    
            else:
                result.append(top_char)
    
                top_freq += 1
                if top_freq != 0:
                    heapq.heappush(max_heap, (top_freq, top_char))
        
        return "".join(result)