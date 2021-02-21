import json
import urllib
import urllib3

class test():
    def __init__(self, url, apikey):
        self.url = url
        self.apikey = apikey

    def translate(self, sentence, src_lan, targ_lan):
        data = {"from":src_lan, "to":targ_lan, "apikey":self.apikey, "src_text": sentence}
        data_en = urllib.urlencode(data)
        req = self.url + "&" + data_en
        res = urllib3.urlopen(req)
        res = res.read()
        res_dict = json.loads(res)
        result = ""
        if (res_dict.has_key("tgt_text")):
            result = res_dict['tgt_text']
        else:
            result = res
        return result

if __name__ == "__main__":
    niutran = test('http://free.niutrans.com/NiuTransServer/translation?','您的apikey' )

    insrc = open("zh.txt","r")
    outsrc = open("zh.txt.big.test","w")
    lines = insrc.readlines()
    for line in lines:
        line = line.strip('\n')
        line = line.strip('\r')
        trans = niutran.translate(line,'zh','en')
        try:
            trans = trans.encode('utf-8')
        except:
            trans = trans
        outsrc.write(trans)

