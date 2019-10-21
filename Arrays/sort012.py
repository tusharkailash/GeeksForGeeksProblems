                                ###Sort an array of 0s, 1s and 2s

#Write a program to sort an array of 0's,1's and 2's in ascending order.

#Solution1:   DUTCH NATIONAL FLAG PROBLEM

class Solution:
     def sorting(self, a):
         low = 0
         high = len(a)-1
         mid = 0

         while mid <= high:
             if a[mid] == 0:
                 a[low], a[mid] = a[mid], a[low]
                 low += 1
                 mid += 1

             if a[mid] == 1:
                 mid += 1      #because 1 is the fixed pole. no changes to it. 0 to its left and 2 to its right

             if a[mid] == 2:
                 a[mid], a[high] = a[high], a[mid]
                 high -= 1     #not decrementing mid as the mid swapped can be 0 to, so we need to check that case

         return a

a = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
print Solution().sorting(a)

#Solution 2:

# class Solution:
#     def sorting(self, nums):
#         i = 0
#         k = 0
#         for j in range(len(nums)):
#             if nums[j] == 0:
#                 temp = nums[i]
#                 nums[i] = nums[j]
#                 nums[j] = temp
#                 i += 1
#         k = i
#         # print nums
#         # print k
#         for j in range(k, len(nums)):
#             if nums[j] == 1:
#                 temp = nums[k]
#                 nums[k] = nums[j]
#                 nums[j] = temp
#                 k += 1
#         print nums
#
# # nums = [0,2,1,2,0]
# nums = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
# print Solution().sorting(nums)