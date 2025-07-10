class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # ⚠️ Issues in Your Approach (Performance-wise):
        # Time Complexity:

        # newlist = nums1 + nums2 → O(n + m)

        # newlist.sort() → O((n + m) log(n + m))

        # n1 in nums1 and n1 in nums2 → both are O(n) in worst case, because in on a list is linear.

        # So overall time complexity is O((n + m) log(n + m) + n(n + m)) → not optimal for large inputs.

        # Unnecessary Sort:

        # Sorting isn’t required here. You only need to find common unique elements.
        # newlist = nums1 + nums2
        # newlist.sort()
        # list = []
        # for i,n1 in enumerate(newlist):
        #     if i > 0 and n1 == newlist[i-1]:
        #         continue
        #     if n1 in nums1 and n1 in nums2:
        #         list.append(n1)
        
        # return list

        # this code will be  O(n + m) Time Complexcity
        set1 = set(nums1)
        set2 = set(nums2)
        result = []

        for num in set1:
            if num in set2:
                result.append(num)
        return result

sol = Solution()

print(sol.intersection([4,9,5],[9,4,9,8,4]))