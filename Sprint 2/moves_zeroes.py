class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lennums = len(nums)
        count_remove = 0
        for i in range(lennums):
            if i < lennums - count_remove:
                if nums[i] == 0:
                    nums.append(nums[i])
                    nums.pop(0)
                    count_remove +=1
        return nums


sol = Solution()

print(sol.moveZeroes([0,0,1]))
