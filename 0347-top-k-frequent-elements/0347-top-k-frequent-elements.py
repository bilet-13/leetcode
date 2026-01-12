class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        min_heap = []
        for num, freq in counter.items():
            heapq.heappush(min_heap, (freq, num))

        return [num for _, num in heapq.nlargest(k, min_heap)]
        