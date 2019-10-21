                            ####First non-repeating character in a stream####
#
# Given an input stream of n characters consisting only of small case alphabets the task is to find the first non repeating character each time a character is inserted to the stream.
#
# Example
#
# Flow in stream : a, a, b, c
# a goes to stream : 1st non repeating element a (a)
# a goes to stream : no non repeating element -1 (5, 15)
# b goes to stream : 1st non repeating element is b (a, a, b)
# c goes to stream : 1st non repeating element is b (a, a, b

# Input:
# 2
# 4
# a a b c
# 3
# a a c
# Output:
# a -1 b b
# a -1 c

#Algo": List1 will contain the duplicates. List2 will contain non duplicates .However, if it it contains same element,
#       we are adding only the first value to the output which is basically the non-repeated element.

tc = int(input())
for i in range(0, tc):
    length = int(input())
    list1 = []
    list2 = []
    char = input()
    strr = ''
    for j in range(0, len(char)):
        # char = input()
        # print (char)

        if char[j] not in list2:
            if char[j] not in list1:
                list2.append(char[j])

            if list2:
                strr += str(list2[0]) + " "
            else:
                strr += "-1 "

        else:
            list2.remove(char[j])
            list1.append(char[j])
            if not list2:
                strr += '-1 '
            else:
                strr += str(list2[0]) + " "
    print (strr)

###########################################################################
#
# def non_Rep(char):
#     list1 = []
#     list2 = []          #contains the first element as the non repeated
#     out = ""
#     for i in range(0,len(char)):
#         if char[i] not in list2:
#             if char[i] not in list1:
#                 list2.append(char[i])
#
#             if list2:
#                 out += str(list2[0]) + " "
#             else:
#                 out += "-1 "
#         else:
#             list2.remove(char[i])
#             list1.append(char[i])
#
#             if list2:
#                 out += str(list2[0]) + " "
#             else:
#                 out += "-1 "
#
#     return out
#
# char = "aabbcd"
# print non_Rep(char)