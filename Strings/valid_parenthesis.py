"""
Given an expression string exp, examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
For example, the program should print 'balanced' for exp = “[()]{}{[()()]()}” and 'not balanced' for exp = “[(])”



Input:

The first line of input contains an integer T denoting the number of test cases.
Each test case consist of a string of expression, in a separate line.

Output:

Print 'balanced' without quotes if pair of parenthesis are balanced else print 'not balanced' in a separate line.


Constraints:

1 ≤ T ≤ 100
1 ≤ |s| ≤ 100


Example:

Input:
3
{([])}
()
()[]

Output:
balanced
balanced
balanced
"""
class Solution(object):
    def isValid(self):
        """
        :type s: str
        :rtype: bool
        """


        s = list(input())
        stack = []
        dict = {'{': '}', '(': ')', '[': ']'}
        for i in s:
            if i in dict:
                stack.append(i)
            else:
                if not stack or (stack and dict[stack.pop()] != i):
                    #print dict[stack.pop()]
                    return False

            return not stack

# s="()[}{}"
# ans =  Solution().isValid(s)
t = int(input())
for _ in range(t):
    print Solution().isValid()


