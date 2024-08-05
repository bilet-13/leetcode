class Solution:
    def _transfer_1d_list(self, matrix):
        numbers = []
        for row in matrix:
            for num in row:
                numbers.append(num)
        return numbers
	
    def _binary_search(self, target, numbers, left, right):
        if left <= right and right < len(numbers):
            middle = (left + right) // 2
            if target == numbers[middle]:
                return True
            elif left == right:
                return False
            elif target > numbers[middle]:
                return self._binary_search(target, numbers, middle+1, right)
            else :
                return self._binary_search(target, numbers, left, middle-1)
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        numbers = self._transfer_1d_list(matrix)
        return self._binary_search(target, numbers, 0, len(numbers)-1)