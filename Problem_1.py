#1. Two Sum
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] not in dic:
                dic[nums[i]] = i
            else:
                return [dic[target-nums[i]], i]


a = Solution()
nums = [3, 3]
target = 6
print(a.twoSum(nums, target))