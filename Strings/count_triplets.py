                    ###Count triplets with sum smaller than a given value

# Given an array of distinct integers and a sum value. Find count of triplets with sum smaller than given sum value. Expected Time Complexity is O(n2).
#
# Examples:
#
# Input : arr[] = {-2, 0, 1, 3}
#         sum = 2.
# Output : 2
# Explanation :  Below are triplets with sum less than 2
#                (-2, 0, 1) and (-2, 0, 3)
#
# Input : arr[] = {5, 1, 3, 4, 7}
#         sum = 12.
# Output : 4
# Explanation :  Below are triplets with sum less than 4
#                (1, 3, 4), (1, 3, 5), (1, 3, 7) and
#                (1, 4, 5)



#Solution 1 : 0(n^3)

"""
def countTriplets(arr, sum):
   
    ans = 0
    for i in range(0, len(arr)):
       for j in range(i+1, len(arr)):
           for k in range(j+1, len(arr)):
               if (arr[i] + arr[j] + arr[k] < sum):
                    ans += 1
    return ans


arr = [5, 1, 3, 4, 7]
sum = 12
print countTriplets(arr, sum)
"""



#Solution 2 : O(n^2)

class Solution:
    def countTriplets(self, arr, sum):

        arr.sort()                             #Sort the array
        n = len(arr)
        ans = 0

        for i in range(0, n-2):             ##As we will haev i = j + 1 and last element in the form of k

            j = i + 1                       #Corner elements. From the next element of i to the last element
            k = n - 1

            while j < k:

                if arr[i] + arr[j] + arr[k] >= sum:
                    k -= 1                      #Reducing k to fix the value lesser than sum
                else:

                    ans += (k-j)
                    j += 1                      #Increment j to final oher triplets for the respective i
        return ans



arr = [5, 1, 3, 4, 7]
sum = 12
print Solution().countTriplets(arr, sum)