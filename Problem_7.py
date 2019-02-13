#7. Reverse Integer
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s=1 if x >0 else -1
        x=x*s
        strx=str(x)
        rst=int((strx[0:])[::-1])
        return rst*s*(rst<0x7FFFFFFF)