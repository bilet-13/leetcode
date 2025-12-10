class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m = len(nums2)

        pq = [(nums1[i] + nums2[0], nums2[0], 0) for i in range(min(k, len(nums1)))]
        heapq.heapify(pq)

        result = []
        while pq:
            cur_sum, n2, idx2 = heapq.heappop(pq)

            result.append([cur_sum - n2, n2])
            if len(result) >= k:
                break


            if idx2 + 1 < m:
                new_sum = cur_sum - n2 + nums2[idx2 + 1]
                heapq.heappush(pq, (new_sum, nums2[idx2 + 1], idx2 + 1))
            
        return result
        