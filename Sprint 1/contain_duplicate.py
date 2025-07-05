class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
            print(seen)
        return False
        

sol = Solution()

print(sol.containsDuplicate([3,2,4,3]))