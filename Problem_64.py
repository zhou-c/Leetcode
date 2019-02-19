#64. Minimum Path Sum
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid[0])
        n = len(grid)
        for i in range(1, m):
            grid[0][i] += grid[0][i-1]
        for j in range(1, n):
            grid[j][0] += grid[j-1][0]
        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]

        return grid[n-1][m-1]