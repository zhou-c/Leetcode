#67. Add Binary
class Solution:
    def addBinary(self, a: 'str', b: 'str') -> 'str':
        two_number_sum = int(a, 2) + int(b, 2)
        return bin(two_number_sum)[2:]