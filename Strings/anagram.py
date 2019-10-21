        ###ANAGRAM OR NOT

"""Given two strings, check whether two given strings are anagram of each other or not. 
An anagram of a string is another string that contains same characters, only the order of characters can be different.
 For example, “act” and “tac” are anagram of each other.
Input:
The first line of input contains an integer T denoting the number of test cases. Each test case consist of two strings in 'lowercase' only,
in a separate line.
 
Output:
Print "YES" without quotes if the two strings are anagram else print "NO".
"""


class Solution():
    def isanagram(self,s1, s2):
        if len(s1) != len(s2):
            return "NO"

        dict = {}

        for i in s1:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        for i in s2:
            if i in dict:
                dict[i] -= 1
            else:
                dict[i] = -1

        for k, v in dict.items():
            if v != 0:
                return "NO"

        return "YES"

s1= "listen"
s2 = "silent"
print Solution().isanagram(s1,s2)
