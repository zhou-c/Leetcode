#53. Maximum Subarray
class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        lis = [nums[0]] + [0] * (len(nums) - 1)
        for i in range(1, len(nums)):
            lis[i] = max(lis[i-1]+nums[i], nums[i])
        return max(lis)