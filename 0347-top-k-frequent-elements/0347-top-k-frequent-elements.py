class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        pq = [(frequency, num) for num, frequency in count.items()]

        return [num for frequency, num in heapq.nlargest(k, pq)]
                
            
        
       


        