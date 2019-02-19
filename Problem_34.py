#34. Find First and Last Position of Element in Sorted Array
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            