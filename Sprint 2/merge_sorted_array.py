class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # len_zero = len(nums1) - m
        # if n > 0 :
        #     for i in range(len_zero):
        #         nums1[m+i] = nums2[i]

        #     swaped = True
        #     while(swaped):
        #         swaped = False
        #         for i in range(len(nums1)-1):
        #             if nums1[i] > nums1[i+1]:
        #                 temp = nums1[i]
        #                 nums1[i] = nums1[i+1]
        #                 nums1[i+1] = temp
        #                 swaped = True

        len_zero = len(nums1) - m
        if n > 0 :
            for i in range(len_zero):
                nums1[m+i] = nums2[i]
            nums1.sort()


        print(nums1)

sol = Solution()
# print(sol.merge([1,2,3,0,0,0],3,[2,5,6],3))
print(sol.merge([4,5,6,0,0,0],3,[1,2,3],3))