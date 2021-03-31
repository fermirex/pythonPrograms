import re
def handle_g_Tag(matched):
    print(matched.groupdict())
    if '<g id="' in matched.groupdict()["g_Tag_content"]:
        lineString_new = re.sub(
            r'(?P<g_Tag_Start><g id=")(?P<g_Tag_Num>.*?)(?P<g_Tag_NumEnd>">)(?P<g_Tag_content>.*?</)(?P<g_Tag_End>g>)',
            handle_g_Tag, lineString)
    try:
        int(matched.groupdict()["g_Tag_Num"])
        lineString_new = '<g' + matched.groupdict()["g_Tag_Num"] + ">" + matched.groupdict()["g_Tag_content"] + "g" + \
                     matched.groupdict()["g_Tag_Num"] + ">"
    except:
        # raise ValueError("the g id include non-number chars")
        lineString_new = "<g_id_include_non_number_char(s)>"
    finally:
        return lineString_new
    


lineString = 'V<g id="2160"><g id="2161">G</g></g>/V<g id="2162"><g id="2163">L</g></g> is also called the phase ratio'
print(lineString)
lineString_new = re.sub(
    r'(?P<g_Tag_Start><g id=")(?P<g_Tag_Num>.*?)(?P<g_Tag_NumEnd>">)(?P<g_Tag_content>.*?</)(?P<g_Tag_End>g>)',
    handle_g_Tag, lineString)

print(lineString_new)