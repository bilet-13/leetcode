class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = [(frequency, num) for num, frequency in Counter(nums).items()]

        return [num for frequency, num in heapq.nlargest(k, pq)]