fileName = "configWrods.bin"

bytesList = []
configWordsList = ["0x01","0xFE"]
for item in  configWordsList:
    bytesList.append(int(item, base=16))

with open(fileName, mode="wb") as f:
    f.write(bytes(bytesList))

