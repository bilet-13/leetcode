class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k

        while left < right:
            mid = (right + left) // 2

            if (arr[mid] + arr[mid + k]) / 2 >= x:
                right = mid
            else:
                left = mid + 1

        return arr[left: left + k]

