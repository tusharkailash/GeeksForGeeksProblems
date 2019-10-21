# Convert array into Zig-Zag fashion
# Given an array of distinct elements, rearrange the elements of array in zig-zag fashion in O(n) time. The converted array should be in form a < b > c < d > e < f.
#
# Example:
# Input:  arr[] = {4, 3, 7, 8, 6, 2, 1}
# Output: arr[] = {3, 7, 4, 8, 2, 6, 1}
#
# Input:  arr[] =  {1, 4, 3, 2}
# Output: arr[] =  {1, 4, 2, 3}

#NOTE: I am setting the flag to True(<) and after every iteratin changing the value of it (>).
#I do the respective operations on flag value. If for example, the flag is true (<) but
#the  arr[i] is not greater than arr[i+1] , i don't swap anything and proceed to next element after changing the value of flag.

class Solution:
    def zigzag(self,arr):
        flag = True     #True indicates < and False indicates >

        for i in range(len(arr)-1):
            if flag is True:
                if arr[i] > arr[i+1]:
                    arr[i],arr[i+1] = arr[i+1],arr[i]
            else:
                if arr[i] < arr[i+1]:
                    arr[i],arr[i+1] = arr[i+1],arr[i]
            flag = bool(1 - flag)

        return arr


arr = [4, 3, 7, 8, 6, 2, 1]
print Solution().zigzag(arr)