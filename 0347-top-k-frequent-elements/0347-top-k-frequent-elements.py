class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # heap 
        # use hash map to store the number of the elememnts
        # time complexity o(n + klogn)
        counter = Counter(nums)
        pq = [(count, num) for num, count in counter.items()]
        heapq.heapify(pq)

        return [num for _, num in heapq.nlargest(k, pq)]

      