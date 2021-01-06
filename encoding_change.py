import chardet

# dir = r"C:/Users/86155/Desktop/rsm/pythonPrograms/"
# with open(dir+"test.txt",'rb') as f:
#     content = f.read()
#     print(content)
#     fileEncodeFormate = chardet.detect(content)
#     print(fileEncodeFormate)
#
# # with open(dir+"test.txt", mode= "r", encoding = fileEncodeFormate['encoding']) as f:
# with open(dir+"test.txt", mode= "r", encoding = 'UTF8') as f:
#     content = f.read()
#     with open(dir+"newSaving/test.txt",mode = "w", encoding="UTF8") as fx:
#         fx.write(content)
#         fx.flush()

# a = b"wba nic"
# print(chardet.detect(a))
# b = a.decode(chardet.detect(a)['encoding'])
# c = b.encode('utf8')
# print(chardet.detect(c))

a = "我我 unicode 编码是我我 unicode 编码是我我 unicode 编码是我我 unicode 编码是"
print("我 unicode 编码是:",a.encode('unicode_escape'))
print(chardet.detect(a.encode('unicode_escape')))
b = a.encode("utf8")
print("我 utf8 编码是:",b)
print("utf8编码预估测试: ", chardet.detect(b))
c = a.encode("ANSI")
print("我 ANSI编码是:", c)
print("ANSI编码预估测试: ", chardet.detect(c))
# d = a.encode('GBK')
# print("我 GBK编码是:", d)
# print("GBK编码预估测试: ", chardet.detect(d))
# e = a.encode('utf32')
# print("我 utf32编码是:", e)
# print("utf32编码预估测试: ", chardet.detect(e))




#unicode: 制定了每个字符的十六进制表示是什么, 比如 “我” 0x3F40 这是两个字节
# UTF8 或者 GBK 是将Unicode写到硬盘里的方法: 0  ->  0x30    0x00000030
# 0x3F40 -> UTF8 写入硬盘 -> 0x3E30AB
# 0x3F40 -> GBK 写入硬盘 -> 0x4F5F6F