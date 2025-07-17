class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_consecutive = 0
        current_value = 0
        for n1 in nums:
            if n1 == 1:
                current_value+=1
            else:
                max_consecutive = max(current_value,max_consecutive)
                current_value = 0
        max_consecutive = max(current_value,max_consecutive)
        return max_consecutive

        

sol = Solution()
print(sol.findMaxConsecutiveOnes([1,0,1,1,0,1]))