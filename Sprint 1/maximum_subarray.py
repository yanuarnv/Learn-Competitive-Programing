class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_value = nums[0]
        current_value = 0
        
        for i,n1 in enumerate(nums):
            if current_value < 0 :
                current_value = 0
            current_value += n1
            max_value = max(current_value,max_value)
        return max_value
            

            
        
        

sol = Solution()
print(sol.maxSubArray([-2,-1]))