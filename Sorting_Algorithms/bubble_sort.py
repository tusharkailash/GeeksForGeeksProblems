                        ###Bubble Sort###

# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
#
# Example:
# First Pass:
# ( 5 1 4 2 8 ) –> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
# ( 1 5 4 2 8 ) –>  ( 1 4 5 2 8 ), Swap since 5 > 4
# ( 1 4 5 2 8 ) –>  ( 1 4 2 5 8 ), Swap since 5 > 2
# ( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.
#
# Second Pass:
# ( 1 4 2 5 8 ) –> ( 1 4 2 5 8 )
# ( 1 4 2 5 8 ) –> ( 1 2 4 5 8 ), Swap since 4 > 2
# ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
# ( 1 2 4 5 8 ) –>  ( 1 2 4 5 8 )
# Now, the array is already sorted, but our algorithm does not know if it is completed. The algorithm needs one whole pass without any swap to know it is sorted.
#
# Third Pass:
# ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
# ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
# ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
# ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )

class Solution(object):
    def bubble_sort(self,arr):
        n = len(arr)
        for i in range(0,n):
            for j in range(0,n-i-1):
                if arr[j] > arr[j+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp

        return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print "Sorted array is: "
print Solution().bubble_sort(arr)




