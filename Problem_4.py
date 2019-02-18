#4. Median of Two Sorted Arrays
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #方法1， 先合并数组再求中位数 复杂度 m+n
        m = len(nums1)
        n = len(nums2)
        nums1 += [0] * n

        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]


        len_nums1 = len(nums1)
        if len_nums1 % 2 == 0:
            return (nums1[len_nums1 // 2] + nums1[len_nums1 // 2 - 1]) / 2
        else:
            return nums1[len_nums1 // 2]

        #方法二 递归 复杂度 log(m+n)
