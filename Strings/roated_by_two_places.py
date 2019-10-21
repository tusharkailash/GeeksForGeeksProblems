# Given two strings, the task is to find if a string ('a') can be obtained by rotating another string ('b') by two places.
# Examples:
#
# Input : a = "amazon"
#         b = "azonam"  // rotated anti-clockwise
# Output : 1
#
# Input : a = "amazon"
#         b = "onamaz"  // rotated clockwise
# Output : 1



class Solution(object):
    def isrotated(self,a,b):
        if a == b[2:] + b[:2] or a == b[-2:] + b[:-2]:
            # print b[2:] + b[:2]
            return True
        else:
            return False
a = "amazon"
b = "azonam"


print Solution().isrotated(a,b)