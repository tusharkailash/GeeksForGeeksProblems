# def calculateSpan(price, n, S):
#     # Span value of first day is always 1
#     S[0] = 1
#
#     # Calculate span value of remaining days by linearly
#     # checking previous days
#     for i in range(1, n):
#         S[i] = 1  # Initialize span value
#
#         # Traverse left while the next element on left is
#         # smaller than price[i]
#         j = i - 1
#         while (j >= 0) and (price[i] >= price[j]):
#             S[i] += 1
#             j -= 1
#
#
# # A utility function to print elements of array
# def printArray(arr, n):
#     for i in range(n):
#         print arr[i]
#
# # Driver program to test above function
# price = [10, 4, 5, 90, 120, 80]
# n = len(price)
# S = [None] * n
#
# # Fill the span values in list S[]
# calculateSpan(price, n, S)
#
# # print the calculated span values
# printArray(S, n)

## O(n^2)
# class Solution(object):
#     def calculateSpan(self,price, n, S):
#
#         S[0] = 1
#         for i in range(1, n):
#             S[i] = 1
#             j = i - 1
#             while (j>=0) and (price[i]>=price[j]):
#                 S[i] += 1
#                 j -= 1
#
#         for i in range(n):
#             print S[i]
#
#
#
# price = [10, 4, 5, 90, 120, 80]
# n = len(price)
# S = [None] * n
# print Solution().calculateSpan(price, n, S)
#####################################################################################################################################
## O(n)

class Solution(object):
    def calculateSpan(self, price, S, n):
        stack = []
        stack.append(0)
        S[0] = 1
        for i in range(1,n):
            while (len(stack)>0) and (price[stack[-1]]<=price[i]):
                stack.pop()

            S[i] = i + 1 if len(stack) <= 0 else i - stack[-1]

            stack.append(i)

        output = []
        for i in S:
            output.append((i))
        print output
        

price = [10, 4, 5, 90, 120, 80]
n = len(price)
S = [None] * n
Solution().calculateSpan(price, S, n)
###############################################################################################

# def calculateSpan(price, S, n):
#     # Create a stack and push index of fist element to it
#     st = []
#     st.append(0)
#
#     # Span value of first element is always 1
#     S[0] = 1
#
#     # Calculate span values for rest of the elements
#     for i in range(1, n):
#
#         # Pop elements from stack whlie stack is not
#         # empty and top of stack is smaller than price[i]
#         while (len(st) > 0 and price[st[-1]] <= price[i]):
#             st.pop()
#
#             # If stack becomes empty, then price[i] is greater
#         # than all elements on left of it, i.e. price[0],
#         # price[1], ..price[i-1]. Else the price[i] is
#         # greater than elements after top of stack
#         S[i] = i + 1 if len(st) <= 0 else (i - st[-1])
#
#         # Push this element to stack
#         st.append(i)
#
#     # A utility function to print elements of array
#
#
# def printArray(arr, n):
#     for i in range(0, n):
#         print arr[i]
#
#     # Driver program to test above function
#
#
# price = [10, 4, 5, 90, 120, 80]
# n = len(price)
# # S = [0 for i in range(len(price) + 1)]
# S = [None] * n
# # Fill the span values in array S[]
# calculateSpan(price, S, n)
#
# # Print the calculated span values
# printArray(S, len(price))


