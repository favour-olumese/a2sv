class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        transpose = []

        for row in range(len(matrix[0])):
            transpose.append([])

        for cols in transpose:
            for i in range(len(matrix)):
                cols.append(0)

        for row_idx in range(len(matrix)):
            for col_idx in range(len(matrix[0])):
                transpose[col_idx][row_idx] = matrix[row_idx][col_idx]

        return transpose