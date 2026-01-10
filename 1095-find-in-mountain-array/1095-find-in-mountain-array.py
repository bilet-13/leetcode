# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
          # so the mountain arr[i] is the incresing arr from 0 to i and decresaing from i to n - 1

        # 1 find the mountain index, and use the index to divide the arr into two parts
        # left part: 0 to i - 1 right part i + 1 to n - 1
        # how to find the mountion, the peak == the first element i where arr[i] > arr[i + 1]
        # so is to F F F T T T find the first T
        # 2 use the index to search target, 
        # search left part first because the result needs the minimum index
        # if we can not find the answer in left part, search the right part
        # reutnr answer or -1 if answer is not found


        def find_mountain_index():
            left = 0
            right = mountainArr.length() - 2

            while left <= right:
                mid = (left + right) // 2

                if mountainArr.get(mid) > mountainArr.get(mid + 1): # legal answer try find the smaller one
                    right = mid - 1
                else:
                    left = mid + 1

            return left

        def binary_search(l, r, increasing):
            left = l
            right = r

            while left <= right:
                mid = (left + right) // 2
                num = mountainArr.get(mid) 

                if num == target:
                    return mid

                elif (num > target and increasing) or (num < target and not increasing):
                    right = mid - 1

                else:
                    left = mid + 1
            
            return -1

        mountain_idx = find_mountain_index() 
        if mountainArr.get(mountain_idx) == target:
            return mountain_idx

        left_part_index = binary_search(0, mountain_idx - 1, increasing=True)
        if left_part_index != -1:
            return left_part_index

        right_part_index = binary_search(mountain_idx + 1, mountainArr.length() - 1, increasing=False)

        return right_part_index
        
        
        