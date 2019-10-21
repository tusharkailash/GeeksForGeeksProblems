# https://www.geeksforgeeks.org/find-pythagorean-triplet-in-an-unsorted-array/
# class Solution():
#     def isTriplet(self,arr):
#         j = 0
#         for i in range(len(arr) - 2):
#             for k in range(j + 1, len(arr)):
#                 for j in range(i + 1, len(arr) - 1):
#                     # Calculate square of array elements
#                     x = arr[i] * arr[i]
#                     y = arr[j] * arr[j]
#                     z = arr[k] * arr[k]
#                     if (x == y + z or y == x + z or z == x + y):
#                         return 1
#         return 0
#
#
# arr = [3, 1, 4, 6, 5]
# print Solution().isTriplet(arr)

class Solution():
    def isTriplet(self,arr):
        for i in range(len(arr)):
            arr[i] = arr[i]*arr[i]
        arr.sort()

        for i in range(len(arr)-1, -1, -1):
            l = 0
            r = i - 1
            while l < r:
                if (arr[l]+arr[r]) == arr[i]:
                    return True
                else:
                    if (arr[l]+arr[r]) < arr[i]:
                        l += 1
                    else:
                        r -= 1

        return False


arr = [3, 1, 4, 6, 5]
print Solution().isTriplet(arr)
