class Solution:
    def _transfer_1d_list(self, matrix):
        return [num for row in matrix for num in row ]
	
    def _binary_search(self, target, numbers, left, right):
        if left < right:
            middle = (left + right) // 2
            if target == numbers[middle]:
                return True
            elif target > numbers[middle]:
                return self._binary_search(target, numbers, middle+1, right)
            else :
                return self._binary_search(target, numbers, left, middle)
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        numbers = self._transfer_1d_list(matrix)
        return self._binary_search(target, numbers, 0, len(numbers))