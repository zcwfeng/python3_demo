# coding=utf-8
'''
    @Author: LCY
    @Contact: lchuanyong@126.com
    @blog: http://http://blog.csdn.net/lcyong_
    @Date: 2018-01-15
    @Time: 19:19
    说明： appid和secretKey为百度翻译文档中自带的，需要切换为自己的
           python2和python3部分库名称更改对应如下：
           httplib      ---->    http.client
           md5          ---->    hashlib.md5
           urllib.quote ---->    urllib.parse.quote
    官方链接：
           http://api.fanyi.baidu.com/api/trans/product/index

'''

import http.client
import hashlib
import json
import urllib
import random
import time

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
# "Please choose the start level or tutorial",
# "Green button eliminates green obstacles.",
# "Cover red button, trigger red obstacle.",
# "Give priority to another piece of blocks.",
# "The location of obstacles can not be placed in hexa block, Remove blocks covered by buttons.",
# "Try the cover button again.",
# "Put another piece away.",
"This is fake level.Eliminating interference blocks with magnifying glass."
];

def baidu_translate(content,source,tgl):
    appid = '20151113000005349'
    secretKey = 'osubCEzlGjzvw8qdQc41'
    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = content
    fromLang = source# 源语言
    toLang = tgl   # 翻译后的语言
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        jsonResponse = response.read().decode("utf-8")# 获得返回的结果，结果为json格式
        js = json.loads(jsonResponse)  # 将json格式的结果转换字典结构
        dst = str(js["trans_result"][0]["dst"])  # 取得翻译后的文本结果
        print(dst) # 打印结果
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()

tgs = ["ara","est","bul","pl","dan","de","ru","fra","fin","kor","nl","cs","rom","pt"]
# tgs = ['jp','fra',"fin"]
def tranlateMultiCountryWords(words,tgs):

    for tg in tgs:
        for key in words:
            baidu_translate(key,'en',tg)
            time.sleep(2)
        print(tg,"-------------------------------\n")

if __name__ == '__main__':
    # while True:
    #     print("请输入要翻译的内容,如果退出输入q")
    #     content = input()
    #     if (content == 'q'):
    #         break
    #     baidu_translate(content)
    tranlateMultiCountryWords(words,tgs)
