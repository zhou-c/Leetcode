#69. Sqrt(x)
class Solution:
    def mySqrt(self, x: 'int') -> 'int':
        under = 0
        upper = x
        while (int(under) != int(upper)):
            middle = (under + upper) / 2
            if middle * middle > x:
                upper = middle
            elif middle * middle < x:
                under = middle
            else:
                return int(middle)
        return int(upper)
        '''
        # Newton
        r = x
        while r * r > x:
            r = (r + x // r) // 2
        return r
        '''