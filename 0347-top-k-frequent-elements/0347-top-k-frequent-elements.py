class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = []
        count = Counter(nums)

        # for num in nums:
        #     count[num] += 1
        
        pq = [(frequency, num) for num, frequency in count.items()]
        return [num for frequency, num in heapq.nlargest(k, pq)]
                
            
        
       


        