                        ###Determine if a string has all Unique Characters

# Given a string, Determine if the string has all unique characters.
# Examples :

# Input : abcd10jk
# Output : true
#
# Input : hutg9mnd!nk9
# Output : false


class Solution(object):
    def isUnique(self,str):
        if not str:
            return
        new_Str = sorted(list(str))
        # print new_Str
        for i in range(len(new_Str)-1):
            if new_Str[i] == new_Str[i+1]:
                return False
            else:
                continue
        return True

str = "hutg9mnd!nk9"
print Solution().isUnique(str)
