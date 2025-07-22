class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new = s.lower()
        new = "".join(c for c in new if c.isalnum())
        r = "".join(reversed(new))
        if r == new:
            return True
        else:
            return False
        

sol = Solution()

print(sol.isPalindrome("man"))