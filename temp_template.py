#-*- coding:utf-8 -*-
import urllib.request
import requests

# 协议
from nntplib import *

# s = NNTP('web.aioe.org')
# (resp, count, first, last, name) = s.group('comp.lang.python')
# (resp, subs) = s.xhdr('subject', (str(first)+'-'+str(last)))
#
# for subject in subs[-10:]:
#     print(subject)
#
# number = input('Which article do you want to read? ')
# (reply, num, id, list) = s.body(str(number))
# for line in list:
#     print(line)


# html=urllib.request.urlopen("http://movie.douban.com/chart").read()
# print(html)
# r = requests.get('https://github.com', timeout=5)
# r = requests.get('https://github.com', timeout=(3.05, 27))
# r = requests.get('https://github.com', timeout=None)


# import json
#
# r = requests.get('http://httpbin.org/stream/20', stream=True)

# for line in r.iter_lines():
#
#     # filter out keep-alive new lines
#     if line:
#         decoded_line = line.decode('utf-8')
#         print(json.loads(decoded_line))

# # 适配器
# s = requests.Session()
# # s.mount('http://www.github.com', MyAdapter())
#
# # 代理
# proxies = {
#   "http": "http://10.10.1.10:3128",
#   "https": "http://10.10.1.10:1080",
# }
#
# requests.get("http://example.org", proxies=proxies)

# 内置函数
# __import__("Tools_whois")

from scapy3k.layers.l2 import getmacbyip

# try:
#     #获取目标的mac
#     tg=getmacbyip("192.168.199.197")
#     print(tg)
# except Exception as f:
#     print('[-]{}'.format(f))


# class A(object):
#     def __init__(self,name,num):
#         self.name = name
#         self.num = num
#
#     def displayName(self):
#         print(self.name)
#
#
# print([int for i in range(0,6)])


from scrapy.utils.url import urljoin_rfc
p  = urljoin_rfc("http://test","ffff","utf-8")
print(p)
