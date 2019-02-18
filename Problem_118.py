#118. Pascal's Triangle
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        triangle = [[0 for i in range(numRows)] for j in range(numRows)]
        triangle[0][0] = 1

        for i in range(1, numRows):
            for j in range(numRows):
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

        new_triangle = []
        for i in range(numRows):
            new_triangle.append(triangle[i][:i+1])
        return new_triangle


