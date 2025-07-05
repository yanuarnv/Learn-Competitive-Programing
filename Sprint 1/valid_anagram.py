class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # time complexcity O(n log n)

        # if len(s) != len(t):
        #     return False
        # if sorted(s) == sorted(t):
        #     return True
        # else:
        #     return False

        # Time complexcity O(n)

        if len(s) != len(t):
            return False

        count = {}
        for char in s:
            #it will be {'a':1} value in dictionary will represent count character in
            # word
            count[char] = count.get(char, 0) + 1

        # the result forloop above is {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}

        for char in t:
            # and check current character in t not in count or if char include value cannot
            # 0 because if char = 'a' and count['a'] == 0 true its mean  'a' > 3
            if char not in count or count[char] == 0:
                return False
            # decrement count value after used
            count[char] -= 1

        return True

        
        

sol = Solution()
print(sol.isAnagram("anagram","nagaram"))