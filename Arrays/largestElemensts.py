# class Solution(object):
#     def largestElements(self, nums, k):
#         output=[]
#         nums.sort()
#         for i in range(len(nums)-1,len(nums)-k-1,-1):
#             output.append(nums[i])
#         return output


class Solution(object):
    def largestElements(self, nums, k):
        output=[]
        nums.sort(reverse=True)
        for i in range(k):
            output.append(nums[i])
        return output


nums = [1, 23, 12, 9, 30, 2, 50]
k =3
print Solution().largestElements(nums, 3)