                            ### MergeSort ###

#https://www.youtube.com/watch?v=TzeBrDU-JaY

#Pseudo code:
# MergeSort(arr[], l,  r)
# If r > l
#      1. Find the middle point to divide the array into two halves:
#              middle m = (l+r)/2
#      2. Call mergeSort for first half:
#              Call mergeSort(arr, l, m)
#      3. Call mergeSort for second half:
#              Call mergeSort(arr, m+1, r)
#      4. Merge the two halves sorted in step 2 and 3:
#              Call merge(arr, l, m, r)

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]

##Steps:##

#Function mergeSort() is used to divide the array into subarrays which are to be sorted. Here, we do recursion.
#Once the array is brought to a position where l=r, we exit from the recursion and call the merge function.
#merge function is used to merge the sub-arrays

def mergeSort(arr,l,r):
    if l<r:
        m = (l + (r-1))/2   #This is similar to (l+r)/2 but is better to avoid overflow for larger values.
        #Recursion next to divide the array to sub-array and then merge and sort.
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

def merge(arr,l,m,r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1   #Left half of the array
    R = [0] * n2   #Right half of the array

    for i in range(0,n1):
        L[i] = arr[l+i]         #Copying the data to Left array

    for j in range(0,n2):
        R[j] = arr[m+1+j]       #Copying the data to Right array

    i = 0
    j = 0
    k = l   #k=0

    #Merging
    while i<n1 and j<n2:
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    #To copy the remaining elements of L[] to arr if any are left out
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # To copy the remaining elements of R[] ro arr if any are left out
    while j <n2:
        arr[k] = R[j]
        j += 1
        k += 1

arr = [2,4,1,6,8,5,3,7]
mergeSort(arr,0,len(arr)-1)
print arr



