

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [-1] * len(nums)
        stack = []
        for i in range(len(
                nums)) * 2:  # Process it twice as it is a circular array to make sure that we can reread the next greater element after every element
            while stack and (nums[stack[-1]] < nums[i]):
                result[stack.pop()] = nums[i]
            stack.append(i)

        return result

numberOfTests = int(input())
for i in range(0, numberOfTests):
    nums = list(input())
    print Solution().nextGreaterElements(nums)

#Note: We basically check the the stacks’s latest element with the next number. If the number is greater than the stack element,
# the res[stack] element becomes the next greatest element.

# Processing ti twice for inout such as [1,3,4,1]
# o/p = [ 3,4,-1,3]