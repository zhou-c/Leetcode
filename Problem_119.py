#119. Pascal's Triangle II
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        #if rowIndex == 1:
            #return [1]
        #阶乘值
        lis = [1, 1]
        for i in range(2, rowIndex+1):
            lis.append(lis[i-1]*i)
        #输出第rowIndex行
        triangle = []
        for i in range(rowIndex+1):
            triangle.append(lis[rowIndex]//(lis[i]*lis[rowIndex-i]))
        return triangle

a = Solution()
print(a.getRow(2))