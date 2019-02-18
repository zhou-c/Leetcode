#11. Container With Most Water
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        arr_len = len(height)
        area = 0
        front = 0
        rear = arr_len - 1
        while front < rear:
            if height[front] < height[rear]:
                h = height[front]
                front += 1
            else:
                h = height[rear]
                rear -= 1
            new_area = h * (arr_len - 1)
            area = max(area, new_area)
            arr_len -= 1
        return area
a = Solution()
print(a.maxArea([1,8,6,2,5,4,8,3,7]))