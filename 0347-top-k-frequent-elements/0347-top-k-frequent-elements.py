class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = []
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        for num, frequency in count.items():
            if len(pq) < k:
                heapq.heappush(pq, (frequency, num))
            elif pq[0][0] < frequency:
                heapq.heappop(pq)
                heapq.heappush(pq, (frequency, num))
        
        return [num for frequency, num in pq]
                
            
        
       


        