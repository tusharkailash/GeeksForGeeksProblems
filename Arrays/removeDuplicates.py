                            ####Remove duplicates from sorted array
# Given a sorted array, the task is to remove the duplicate elements from the array.
#
# Examples:
#
# Input  : arr[] = {2, 2, 2, 2, 2}
# Output : arr[] = {2}
#          new size = 1
#
# Input  : arr[] = {1, 2, 2, 3, 4, 4, 4, 5, 5}
# Output : arr[] = {1, 2, 3, 4, 5}
#          new size = 5

class Solution(object):
    def removeDuplicates(self, arr):
        n = len(arr)
        if n == 0 or n == 1:
            return n

        # To store index of next  unique element
        j = 0

        for i in range(0, n-1):
            if arr[i] != arr[i+1]:
                arr[j] = arr[i]
                j += 1

        arr[j] = arr[n-1]    #The last element of the unique array
        j += 1
        return j

arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
newlength =  Solution().removeDuplicates(arr)

for i in range(newlength):
    print arr[i]
