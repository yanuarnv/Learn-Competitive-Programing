class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # lennums = len(nums)
        # for i in range(lennums):
        #     if nums[i] == 0:
        #             nums.append(nums[i])
        #             nums.remove(0)
        # return nums

        insert_pos = 0
   
        # Langkah 1: Geser semua non-zero ke depan
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1
                
        # Langkah 2: Isi sisa posisi dengan 0
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1

        return nums


sol = Solution()

print(sol.moveZeroes([0, 1, 0, 3, 12]))
