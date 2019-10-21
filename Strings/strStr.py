###Implement strstr (Function Problem)###



class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m = len(haystack)
        n = len(needle)

        if n == 0:
            return 0

        if m < n:
            return -1

        for i in range(m - n + 1):
            for j in range(n):
                if haystack[i + j] != needle[j]:
                    break  # come out of the j loop
                else:
                    if j == n - 1:
                        return i  # Trick:once the letters start to match, this condition will be true only at the last letter of haystack
                        # and the result will be obtained.
        return -1





inp = input()
for i in range(inp):
    haystack = list(input())
    needle = list(input())
    print Solution().strStr(haystack, needle)