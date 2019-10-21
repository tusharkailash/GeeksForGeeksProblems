"""
Given an string in roman no format (s)  your task is to convert it to integer .

Input:
The first line of each test case contains the no of test cases T. Then T test cases follow. Each test case contains a string s denoting the roman no.

Output:
For each test case in a new line print the integer representation of roman number s.

Constraints:
1<=T<=100
1<=roman no range<4000

Example:
Input
2
V
III
Output
5
3
"""

class Solution(object):
    def romanToInt(self):
        """
        :type s: str
        :rtype: int
        """
        dict = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        numberOfTests = int(input())
        for i in range(0, numberOfTests):
            s = input()                     #take the inputs from user
            result = dict[s[-1]]            # last element of input
            #print result
            for i in range(len(s) - 2, -1, -1):
                if dict[s[i]] < dict[s[i + 1]]:
                    result -= dict[s[i]]
                else:
                    result += dict[s[i]]
            print result


print Solution().romanToInt()


