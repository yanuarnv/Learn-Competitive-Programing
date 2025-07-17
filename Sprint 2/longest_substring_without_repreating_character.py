class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        sets =set()
        max_longest = 0
        l = 0
        for r in range(len(s)):
            while s[r] in sets:
                sets.remove(s[l])
                l+=1
            sets.add(s[r])
            max_longest = max(max_longest,r-l+1)
        return max_longest

sol = Solution()
print(sol.lengthOfLongestSubstring("a"))