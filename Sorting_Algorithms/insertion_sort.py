                    ###Insertion Sort###
                    
#Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.
#Another Example:
# 12, 11, 13, 5, 6
#
# Let us loop for i = 1 (second element of the array) to 5 (Size of input array)
#
# i = 1. Since 11 is smaller than 12, move 12 and insert 11 before 12
# 11, 12, 13, 5, 6
#
# i = 2. 13 will remain at its position as all elements in A[0..I-1] are smaller than 13
# 11, 12, 13, 5, 6
#
# i = 3. 5 will move to the beginning and all other elements from 11 to 13 will move one position ahead of their current position.
# 5, 11, 12, 13, 6
#
# i = 4. 6 will move to position after 5, and elements from 11 to 13 will move one position ahead of their current position.
# 5, 6, 11, 12, 13

class Solution(object):
    def insertionSort(self,arr):

        for i in range(1,len(arr)):
            key = arr[i]                #current element
            j = i - 1

            while j>=0 and key<arr[j]:  #loop continues until the least value is moved to its respective position.
                arr[j+1] = arr[j]       #basically shifting the positions for making place to the least value
                j -= 1
            arr[j+1] = key              #least value is moved here


arr = [12, 11, 13, 5, 6]
print Solution().insertionSort(arr)


#printed arr inside while loop to see the results
# [12, 12, 13, 5, 6]
# arr[j+1]=11
# [11, 12, 13, 5, 6]
# arr[j+1]=13
# [11, 12, 13, 5, 6]
# [11, 12, 13, 13, 6]
# [11, 12, 12, 13, 6]
# [11, 11, 12, 13, 6]
# arr[j+1]=5
# [5, 11, 12, 13, 6]
# [5, 11, 12, 13, 13]
# [5, 11, 12, 12, 13]
# [5, 11, 11, 12, 13]
# arr[j+1]=6
# [5, 6, 11, 12, 13]
# None
