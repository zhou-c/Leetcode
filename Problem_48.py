#48. Rotate Image
class Solution:
    def rotate(self, matrix: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return []
        l = len(matrix)
        for i in range(l // 2):
            for j in range(i,l - 1 - i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[l - 1 - j][i]
                matrix[l - 1 - j][i] = matrix[l - 1 - i][l - 1 - j]
                matrix[l - 1 - i][l - 1   - j] = matrix[j][l - 1 -i]
                matrix[j][l - 1 - i] = temp