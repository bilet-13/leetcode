class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)

        max_count = max(counter.values())
        if max_count > math.ceil(len(s) / 2):
            return ""

        max_pq = [(-count, char) for char, count in counter.items()]
        heapq.heapify(max_pq)

        result = []
        while len(max_pq) >= 2:
            count1, ch1 = heapq.heappop(max_pq) 
            count2, ch2 = heapq.heappop(max_pq) 

            result.extend([ch1, ch2])

            if count1 + 1 != 0:
                heapq.heappush(max_pq, (count1 + 1, ch1))

            if count2 + 1 != 0:
                heapq.heappush(max_pq, (count2 + 1, ch2))
        
        if max_pq:
            _, ch = heapq.heappop(max_pq)
            result.append(ch)

        return "".join(result)
        



            

        