import re

# re.match(pattern, string, flags=0)
# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。


# samplerString = "etest13gfbsfaa23"
#
# result = re.search(r'\d{3}',samplerString)
# # result2 = re.findall(r'\d',samplerString)
# print(result.span())
# # print(result2)
#
# #\d{2}  == \d\d
# #<g id="71">des12_fuel_cap</g>.
# #<g id=".8?>.*?</g>
# re.compile("")

# import re
# # 将匹配的数字乘以 2
# def double(matched):
#     value = int(matched.group('value'))
#     return str(value * 2)
#
#
# s = 'A23G4HFD567'
# print(re.sub('(?P<value>\d+)', double, s))  #(?P<tag>\d+) 分组匹配，print(res.groupdict())
# {'province': '110', 'city': '223', 'born_year': '1990'}

def handle_g_Tag(matched):
    print(matched.groupdict())
    try:
        int(matched.groupdict()["g_Tag_Num"])
        lineString_new = '<g' + matched.groupdict()["g_Tag_Num"] + ">" + matched.groupdict()["g_Tag_content"] + "g" + \
                     matched.groupdict()["g_Tag_Num"] + ">"
    except:
        # raise ValueError("the g id include non-number chars")
        lineString_new = "<g_id_include_non_number_char(s)>"
    finally:
        return lineString_new

# with open("filepath", mode="a+", encoding="UTF8") as f:
#     while True:
#         lineString = f.readline()

lineString = '# Click <g id="90">OK</g> to acknowledge the warning <g id="10o">OK</g> message.'
print(lineString)
lineString_new = re.sub(r'(?P<g_Tag_Start><g id=")(?P<g_Tag_Num>.*?)(?P<g_Tag_NumEnd>">)(?P<g_Tag_content>.*?</)(?P<g_Tag_End>g>)',handle_g_Tag,lineString)

print(lineString_new)
# Click <g id="90">OK</g> to acknowledge the warning message.
# Click <g90>OK</g90> to acknowledge the warning message.
