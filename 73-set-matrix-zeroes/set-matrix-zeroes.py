class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])

        is_there_0_in_rows = any(matrix[0][j] == 0 for j in range(n))
        is_there_0_in_columns = any(matrix[i][0] == 0 for i in range(m))

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if is_there_0_in_rows:
            for j in range(n):
                matrix[0][j] = 0
        if is_there_0_in_columns:
            for i in range(m):
                matrix[i][0] = 0                   





       
        