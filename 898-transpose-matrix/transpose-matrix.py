class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        row, column = len(matrix), len(matrix[0])

        transpose_matrix = [[0] * row for _ in range(column)]

        for i in range(row):
            for j in range(column):
                transpose_matrix[j][i] = matrix[i][j]
        return transpose_matrix        
        