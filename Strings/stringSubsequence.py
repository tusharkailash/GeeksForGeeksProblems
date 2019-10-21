# Given two strings, find if first string is a subsequence of second
# Given two strings str1 and str2, find if str1 is a subsequence of str2. A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements (source: wiki). Expected time complexity is linear.
#
# Examples :
#
# Input: str1 = "AXY", str2 = "ADXCPY"
# Output: True (str1 is a subsequence of str2)
#
# Input: str1 = "AXY", str2 = "YADXCP"
# Output: False (str1 is not a subsequence of str2)

class Solution(object):
    def isSubSequence(self,str1,str2):

        j = 0    # Index of str1
        i = 0    # Index of str2 (largest string)
        m = len(str1)
        n = len(str2)

        while j<m and i<n:
            if str1[j] == str2[i]:
                j = j+1
            i = i + 1

        # If all characters of str1 matched, then j is equal to m
        if j == m:
            return True
        else:
            return False


str1 = "gksrek"
str2 = "geeksforgeeks"
print Solution().isSubSequence(str1,str2)
