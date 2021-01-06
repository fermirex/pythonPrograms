import re

# re.match(pattern, string, flags=0)
# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。


samplerString = "etest13gfbsfaa23"

result = re.search(r'\d{3}',samplerString)
# result2 = re.findall(r'\d',samplerString)
print(result.span())
# print(result2)

#\d{2}  == \d\d