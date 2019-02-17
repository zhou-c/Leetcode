class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        newS = s.strip()
        return len(newS.split(' ')[-1])