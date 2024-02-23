class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        str_matrix = []
        str_matrix_reverse = [[0 for i in range(len(strs))] for i in range(len(strs[0]))]
        total = 0

        for string in strs:
            str_matrix.append(list(string))

        print('Hello',str_matrix_reverse)

        for i in range(len(str_matrix)):
            for j in range(len(str_matrix[0])):
                str_matrix_reverse[j][i] = str_matrix[i][j]

        for strs in str_matrix_reverse:
            if sorted(strs) != strs:
                total += 1

        return total