def removeLf(inputLines):
    LfCounter = 0
    spaceCounter = 0
    if type(inputLines) != str:
        raise TypeError("input parameters must be string")
    spaceNum = len(inputLines) - len(inputLines.rstrip())
    if spaceNum == len(inputLines):
        raise ValueError("input Empty lines")
    while spaceCounter < spaceNum :
        if inputLines[-1] == "\n":
            inputLines = inputLines[:-1]
            LfCounter += 1
            spaceCounter += 1
        inputLines = inputLines[:-1]
        spaceCounter += 1
    return inputLines, LfCounter

testString = "test remove the space \r\n\t\n\t"
# testString = '\r\n'
newSting, lfConter = removeLf(testString)
print(newSting + "-with remove {} times LF".format(lfConter))