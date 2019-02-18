#15. 3Sum
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        arr = []
        if not nums:
            return []
        #进行排序
        nums.sort()
        for i in range(len(nums)):
            x = []
            for j in range(i+1, len(nums)):
                if (-(nums[i] + nums[j]) in nums[j+1:]) and (nums[j] not in x):
                    arr.append([nums[i], nums[j], -(nums[i] + nums[j])])
                    x.append(nums[j])
        return arr
a = Solution()
print(a.threeSum([-1, 0, 1, 2, -1, -4]))