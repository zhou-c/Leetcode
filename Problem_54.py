#54. Spiral Matrix
class Solution:
    def spiralOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        if not matrix:
            return []
        num_row = len(matrix)
        num_col = len(matrix[0])
        output = []
        while num_row or num_col > 0:
            pass