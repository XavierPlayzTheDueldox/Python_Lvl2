from ex104 import readval, sortedvalue

def reverseorder(inp):
    newlist = list()
    for i in range(len(inp)):
        newlist.append(inp[-1])
        inp.remove(inp[-1])
    return newlist

print(reverseorder(sortedvalue(readval('Enter a number. Enter 0 to proceed.','0'))))