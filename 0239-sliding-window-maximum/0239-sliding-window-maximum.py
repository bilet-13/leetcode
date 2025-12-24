class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
         # brute force find max element of the window in each time
        # time complexity o(nk) n == len(nums)

        # max heap to get the maximum the element in window is (num, count) 
        # and when the window move if the pop element == top of the heap count -= 1 
        # and pop the lement when the count is 0
        # if the leftover element != top of the heap that means the elemnt is not max elemnt of previous widnow
        # don't need to do anything
        # use a list to store the result
        # hash map to store the element_in_window

        # use hash map to check the max element of heap is in current window
        # use max heap to store the max possible candidates
        # how to simplify it 

        max_elements = []
        cur_window_elements = defaultdict(int)
        max_pq = []

        for right in range(len(nums)):
            num = nums[right]

            cur_window_elements[num] += 1
            heapq.heappush(max_pq, -num)

            while max_pq and cur_window_elements[-max_pq[0]] <= 0:
                heapq.heappop(max_pq) 


            left = right - k + 1
            if left >= 0:
                max_elements.append(-max_pq[0])
                
                pop_element = nums[left]
                cur_window_elements[pop_element] -= 1

        return max_elements

            

