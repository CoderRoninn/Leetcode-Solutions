class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        for row in range(len(triangle)-2,-1,-1):
            for column in range(row+1):
                triangle[row][column] += min(triangle[row + 1][column], triangle[row + 1][column + 1])

        return triangle[0][0]        
        