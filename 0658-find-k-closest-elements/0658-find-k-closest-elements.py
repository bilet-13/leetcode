class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
             # two pointer
        # so the sliding window size is k
        # hash map to store the key: index and val: the close point == abs(a - x) for any a
        # move sliding window until the new element is not closet compare to leftover elemtn
        # when stop use return arr[left: left + k] 
        left = 0
        result_left = 0
        cur_closest_sum = sum(abs(num - x) for num in arr[:k])
        min_closest_sum = cur_closest_sum 

        for right in range(k, len(arr)):
            cur_closest_sum += abs(arr[right] - x) - abs(arr[right - k] - x)

            if cur_closest_sum < min_closest_sum:
                min_closest_sum = cur_closest_sum
                result_left = right - k + 1
        
        return arr[result_left: result_left + k] 
        