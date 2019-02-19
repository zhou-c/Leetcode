#55. Jump Game
class Solution:
    def canJump(self, nums: 'List[int]') -> 'bool':
        if not nums:
            return False
        maxl = nums[0]
        for i in range(len(nums)):
            if maxl >= i:
                maxl = max((i + nums[i]), maxl)
            else:
                return False
        if maxl >= len(nums) - 1:
            return True
        else:
            return False