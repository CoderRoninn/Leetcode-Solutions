class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        row, column = len(matrix), len(matrix[0])

        left, right = 0, (row * column) -1

        while left <= right:

            middle = left + (right - left) // 2

            if matrix[middle // column][middle % column] == target:
                return True
            elif matrix[middle // column][middle % column] > target:
                right = middle -1
            else:
                left = middle + 1
        return False            

        