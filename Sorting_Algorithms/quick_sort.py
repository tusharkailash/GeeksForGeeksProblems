                                ###QuickSort###

# https://www.youtube.com/watch?v=COk73cpQbFQ

# The key process in quickSort is partition().
# Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array
#and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x.
# All this should be done in linear time.

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        # Separately sort elements before partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

# This function takes last element as pivot, places the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot) to left of pivot and all greater elements to right of pivot

def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]      # pivot. last value.

    for j in range(low, high):

        if arr[j] <= pivot: # If current element is smaller than or equal to pivot
            i = i + 1  # increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  #swap the i+1 element with the pivot element.
    return (i + 1)



arr = [7,2,1,6,8,5,3,4]
n = len(arr)
quickSort(arr, 0, n - 1)
print arr

