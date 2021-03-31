import re


st = 'Press <x id=  "63"/>OCP State <x id="64"/>ON | OFF to enable over-current protection.'
# def all_tag_extract(st):
#     pt = re.compile('<..id="\d.*?">|<..id="\d.*?"/>')
#     it = re.finditer(pt, st)
#     tag_set = []
#     for i in it:
#         print(i.group())
#         dd = re.findall(r'\d+', i.group())
#         tag_set.extend(dd)
#     return tag_set
#print(all_tag_extract(st))
# def double(matched):
#     value = int(matched.group('value'))
#     return "<x"+str(value)+"/>"
# #s = 'A23G4HFD567'
# pt = re.compile('<x id="\d.*?"/>')
# print(re.sub('(?P<value>pt)', double, st))

def handle_x_Tag(matched):
    print(matched.groupdict())
    try:
        int(matched.groupdict()["x_Tag_Num"])
        lineString_new = '<x' + matched.groupdict()["x_Tag_Num"] + "/>"
    except:
        # raise ValueError("the g id include non-number chars")
        lineString_new = "<g_id_include_non_number_char(s)>"
    finally:
        return lineString_new
lineString = 'Press <x id=  "63"/>OCP State <x id="64"/>ON | OFF to enable over-current protection.'
# lineString = 'Press <x63/>OCP State <x64/>ON | OFF to enable over-current protection.'
#               Press <x63/>OCP State <x64/>ON | OFF to enable over-current protection.
print(lineString)
lineString_new = re.sub(
    r'(?P<x_Tag_Start><x id=.*?")(?P<x_Tag_Num>.*?)(?P<x_Tag_NumEnd>"/>)',handle_x_Tag, lineString)
print(lineString_new)