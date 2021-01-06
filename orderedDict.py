import os
import logging
import collections

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

FilePath = r"C:\Users\M&M\Desktop\pro-zh"
FileList = os.listdir(FilePath)
if "static.txt" in FileList:
    FileList.pop(FileList.index('static.txt'))
logger.info(f'Files in path {FilePath} are: {FileList}')

orderedDict = collections.OrderedDict()

with open(FilePath + r"\static.txt", mode="w+", encoding="UTF8") as staticFile:
    for file in FileList:
        for fileLine in open( FilePath+'\\'+file, mode="r", encoding="UTF8"):
            logger.info(f'read line: [{fileLine.strip()}] from: {file}')
            keyAndValueList = fileLine.strip().split('\t')
            logger.info(f'split the line: {fileLine.strip()} as list: {keyAndValueList}')
            try:
                currentValue = orderedDict[keyAndValueList[0]]
                logger.info(f'currentValue in orderedDick of {keyAndValueList[0]} is {currentValue}')
            except:
                logger.warning(f"there have no key {keyAndValueList[0]} in orderedDick")
                currentValue = 0

            if currentValue:
                orderedDict[keyAndValueList[0]] = currentValue + int(keyAndValueList[1])
                logger.info(f'add the new value: {keyAndValueList[1]} + {currentValue} to the ordered dict key: {keyAndValueList[0]}')
            else:
                orderedDict[keyAndValueList[0]] = int(keyAndValueList[1])
                logger.info(f'add the new value: {keyAndValueList[1]} to the ordered dict key: {keyAndValueList[0]}')

    for key, value in orderedDict.items():
        logger.info(f"write the strint: {key} + '\t' + {str(value)} ")
        staticFile.write(key + '\t' + str(value)+ '\n')