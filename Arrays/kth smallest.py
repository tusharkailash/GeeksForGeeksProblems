                            ### Kth Smallest/Largest Element in Unsorted Array ###
#
# Given an array and a number k where k is smaller than size of array, we need to find the kth smallest element \
# in the given array. It is given that ll array elements are distinct.
#
# Examples:
#
# Input: arr[] = {7, 10, 4, 3, 20, 15}
#        k = 3
# Output: 7
#
# Input: arr[] = {7, 10, 4, 3, 20, 15}
#        k = 4
# Output: 10

class Solution:
    def kthSmallest(self, arr):

        arr.sort()
        return arr[k-1]   #for kth smallest

        # return arr[len(arr) - k]   #for kth largest

arr = [12,5,3,7,19]
k = 2
print Solution().kthSmallest(arr)