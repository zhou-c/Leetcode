#70. Climbing Stairs
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)
    #使用递归时间过长
    '''
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a
    '''