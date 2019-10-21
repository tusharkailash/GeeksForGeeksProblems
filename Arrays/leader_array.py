
                                ###Leaders in an array###

# Write a program to print all the LEADERS in the array.
#An element is leader if it is greater than all the elements to its right side. The rightmost element is always a leader.

# Solution 1 : O(n2)

# class Solution:
#     def leader(self,nums):
#         ans = []
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[j] > nums[i]:
#                     break
#                 elif j == len(nums) - 1:
#                     ans.append(nums[i])
#         ans.append(nums[-1])
#         return ans
#
#         #     ans.append(nums[i])             #Since we want the last element as the leader too
#         # return ans
#
#
# # nums = [16,17,4,3,5,2]
# nums = [15,4,3,20,7,10,18,1]
# print Solution().leader(nums)


# Solution 2: O(n)

class Solution:
    def leader(self,nums):
        ans = []
        max = nums[-1]
        ans.append(max)                     #Since we want the last element as the leader too
        for i in range(len(nums)-2,0,-1):
            if nums[i] > max:
                max = nums[i]
                ans.append(nums[i])
        return ans[::-1]

# nums = [16,17,4,3,5,2]
nums = [15,4,3,20,7,10,18,1]
print Solution().leader(nums)