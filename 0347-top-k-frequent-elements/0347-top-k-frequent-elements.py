class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # heap 
        # use hash map to store the number of the elememnts
        # time complexity o(n + ulogk)
        counter = Counter(nums)
        pq = []

        for num, count in counter.items():
            heapq.heappush(pq, (count, num))

            if len(pq) > k:
                heapq.heappop(pq)

        return [num for _, num in pq]

      