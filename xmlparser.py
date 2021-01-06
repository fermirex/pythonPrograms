import xml.etree.ElementTree as ET

xmlPath = "C:\\Users\\86155\\Desktop\\GuoM\\11.14\\"
xmlFileName = "MicrosoftTermCollection_en-US_zh-CN.tbx"
xmlParserFileName = "tbx_File_Parser_Result.txt"

tree = ET.parse( xmlPath +  xmlFileName)
# root = tree.getroot()


with open(xmlPath +xmlParserFileName, mode="w+", encoding="UTF8") as f:
    # termEntryCounter = 0
    # termElementCounter = 0
    for elem in tree.iter(tag= "termEntry"):
        # if termElementCounter > 2:
        #     f.write("!!!!!!!!!!!!!!!!!!!!!!!!!!More than !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\r\n")
        # termEntryCounter += 1
        # f.write("---------------termEntryCounter: {}----------------".format(termEntryCounter)+ "\r\n")
        # f.write(elem.tag+" "+ str(elem.attrib)+" "+ str(elem.text)+ "\r\n")
        # termElementCounter = 0
        for termElement in elem.iter(tag = "term"):
            # termElementCounter += 1
            f.write(termElement.text + " ")
        f.write("\n")


