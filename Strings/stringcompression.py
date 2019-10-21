from collections import OrderedDict

def runLengthEncoding(input):
    # Generate ordered dictionary of all lower
    # case alphabets, its output will be
    # dict = {'w':0, 'a':0, 'd':0, 'e':0, 'x':0}
    dict = OrderedDict.fromkeys(input, 0)
    # print dict            OrderedDict([('w', 4), ('a', 3), ('d', 1), ('e', 1), ('x', 6)])

    for ch in input:
        dict[ch] += 1
    # print dict            OrderedDict([('w', 4), ('a', 3), ('d', 1), ('e', 1), ('x', 6)])

    # now iterate through dictionary to make
    # output string from (key,value) pairs
    output = ''
    for key, value in dict.iteritems():
        output = output + key + str(value)
    return output


input = 'wwwwaaadexxxxxx'
print runLengthEncoding(input)