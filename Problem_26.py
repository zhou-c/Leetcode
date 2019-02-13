#26. Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        else:
            num = 0
            for i in range(1, len(nums)):
                if nums[i] != nums[num]:
                    num += 1
                    nums[num] = nums[i]
            return num + 1

a = Solution()
print(a.removeDuplicates([1, 1, 2]))
