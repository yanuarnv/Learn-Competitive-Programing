class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # newlist = nums1 + nums2
        # newlist.sort()
        # list = []
        # for i,n1 in enumerate(newlist):
        #     if i > 0 and n1 == newlist[i-1]:
        #         continue
        #     if n1 in nums1 and n1 in nums2:
        #         list.append(n1)
        
        # return list

        set1 = set(nums1)
        set2 = set(nums2)
        result = []

        for num in set1:
            if num in set2:
                result.append(num)
        return result

sol = Solution()

print(sol.intersection([4,9,5],[9,4,9,8,4]))