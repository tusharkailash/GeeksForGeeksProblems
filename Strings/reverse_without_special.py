                        ###Reverse an array without affecting special characters

# Reverse an array without affecting special characters
# Given a string, that contains special character together with alphabets, reverse the string in#
# a way that special characters are not affected.
#
# Examples:
#
# Input:   str = "a,b$c"
# Output:  str = "c,b$a"
# Note that $ and , are not moved anywhere.
# Only subsequence "abc" is reversed
#
# Input:   str = "Ab,c,de!$"
# Output:  str = "ed,c,bA!$"



class Solution:
    def reverse(self, str):

        ##STEP1: Convert the string to array

        arr = []
        for i in str:
            arr.append(i)
        # print arr

        l = 0
        r = len(arr) - 1

        while l < r:
            if not arr[l].isalpha():
                l += 1
            elif not arr[r].isalpha():
                r -= 1
            else:
                arr[l] , arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        # print arr

        return "".join(arr)


str = "a!!!b.c.d,e'f,ghi"

print "Input string:  {}".format(str)
ans = Solution().reverse(str)
print "Output string: {}".format(ans)


