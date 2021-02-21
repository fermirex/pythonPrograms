import json
import urllib
import urllib2
import sys
def translate(sentence,src_lan,tgt_lan,apikey):
    url = 'http://free.niutrans.com/NiuTransServer/translation?'
    data = {"from":src_lan, "to":tgt_lan, "apikey":apikey, "src_text": sentence}
    data_en= urllib.urlencode(data)
    req = url +"&"+ data_en
    res = urllib2.urlopen(req)
    res = res.read()
    res_dict = json.loads(res)
    result=""
    if(res_dict.has_key("tgt_text")):
        result = res_dict['tgt_text']
    else:
        result = res
    return result
if __name__=="__main__":
    insrc = open("zh.txt","r")
    outsrc = open("zh.txt.big.test","w")
    lines = insrc.readlines()
    for line in lines:
        line = line.strip('\n')
        line = line.strip('\r')
        trans = translate(line,'zh','en','您的apikey')
        try:
            trans = trans.encode('utf-8')
        except:
            trans = trans
        outsrc.write(trans)