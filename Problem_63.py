#63. Unique Paths II
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)
        matrix = [[0 for i in range(m+1)] for j in range(n+1)]
        matrix[0][1] = 1
        for i in range(1, n+1):
            for j in range(1, m+1):
                matrix[i][j] = obstacleGrid[i-1][j-1]
                if matrix[i][j] == 1:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        return matrix[n][m]

a = Solution()
print(a.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))