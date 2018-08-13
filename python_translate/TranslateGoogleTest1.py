import regex as re
import urllib
url_google = 'http://translate.google.cn'
reg_text = re.compile(r'(?<=TRANSLATED_TEXT=).*?;')
user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                  r'Chrome/44.0.2403.157 Safari/537.36'

def translateGoogle(text, f='ja', t='zh-cn'):
    values = {'hl': 'zh-cn', 'ie': 'utf-8', 'text': text, 'langpair': '%s|%s' % (f, t)}
    value = urllib.parse.urlencode(values)
    req = urllib.request.Request(url_google + '?' + value)
    req.add_header('User-Agent', user_agent)
    response = urllib.request.urlopen(req)
    content = response.read().decode('utf-8')
    data = reg_text.search(content)
    result = data.group(0).strip(';').strip('\'')
    print(result)

from googletrans import  translator

def translateGoogle2(text):
    result = translator.translate(text)
    print(result)

# EN,JP,FR,IT,KR,RU,ES,NO,FI,DK

def translateMultiCcountry(text,tgs):
    for key in tgs:
        # print(key)
        translateGoogle(text,'en',key)

def tranlateMultiCountryWords(words,tgs):

    for tg in tgs:
        for key in words:
            translateGoogle(key,'en',tg)
        print(tg,"-------------------------------\n")


tgs = ["ja","fr","it","ko","ru","da","no","fi","sv","de"]

# translateGoogle("hello",'en','fr')
# translateMultiCcountry("Move block to fill up the board",tgs)





words=[
# "Daily Gift",
# "Setting",
# "Shop",
# "Pause",
# "Sound",
# "Music",
# "Onetime Offer",
# "Happy Easter",
# "OK",
# "Restore",
# "Term of Service",
# "private policy",
# "Remove Adds",
# "More",
# "Today",
# "7Days Event",
# "Play everyday get more rewards",
# "NEXT",
# "Completed",
# "Play",
# "Do you want to continue to play the current level",
# "Tutorial",
# "Skip",
# "Move block to fill up the board",
# "This is Fake level.Beware of the tricks of the extra blocks!",
"Please choose the start level or tutorial"

];



tranlateMultiCountryWords(words,tgs)






