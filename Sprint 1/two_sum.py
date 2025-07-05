# LeetCode 

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """       
        # using current + x = target
        # time O(n)
        map = {}
        for i,num in enumerate(nums):
             value = target - num
             if value in map:
                  return [i,map[value]]
             map[nums[i]] = i



sol = Solution()

print(sol.twoSum([3,2,4],6))
        