def printClosest(arr, x):
    # To store indexes of result pair
    MAX_VAL = diff = float("inf")
    res_l, res_r = 0, 0
    l = 0
    r = len(arr) - 1

    while l<r:

        if abs(arr[l] + arr[r] - x) < diff:
            res_l = l
            res_r = r
            diff = abs(arr[l] + arr[r] - x)

        if arr[l] + arr[r] > x:
           r -= 1
        else:
            l += 1

    print('The closest pair is {} and {}'.format(arr[res_l], arr[res_r]))

arr = [10, 22, 28, 29, 30, 40]
x = 54
printClosest(arr,x)