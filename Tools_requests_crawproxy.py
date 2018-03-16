#python爬西刺代理
import requests
import re
# import dauk
from bs4 import BeautifulSoup
import time
def daili():
  print('[+]极速爬取代理IP，默认为99页')
  for b in range(1,99):
    url="http://www.xicidaili.com/nt/{}".format(b)
    header={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:58.0) Gecko/20100101 Firefox/48.0'}
    r=requests.get(url,headers=header)
    gsx=BeautifulSoup(r.content,'html.parser')
    for line in gsx.find_all('td'):
        sf=line.get_text()
        dailix=re.findall('(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)',str(sf))
        for g in dailix:
            po=".".join(g)
            print(po)
            with open ('采集到的IP.txt','a') as l:
                l.write(po+'\n')

daili()

# def dailigaoni():
#     print('[+]极速爬取代理IP，默认为99页')
#     for i in range(1,99):
#         url="http://www.xicidaili.com/nn/{}".format(i)
#         header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1 Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
#         r=requests.get(url,headers=header)
#         bks=r.content
#         luk=re.findall('(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)',str(bks))
#         for g in luk:
#             vks=".".join(g)
#             print(vks)
#             with open('采集到的IP.txt','a') as b:
#                 b.write(vks+'\n')
# dailigaoni()


# def dailihtp():
#     print('[+]极速爬取代理IP，默认为99页')
#     for x in range(1,99):
#         header="{'User-Agent':'Mozilla/5.0 (Windows NT 6.1 Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}"
#         url="http://www.xicidaili.com/wn/{}".format(x)
#         r=requests.get(url,headers=header)
#         gs=r.content
#         bs=re.findall('(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)',gs)
#     for kl in bs:
#         kgf=".".join(kl)
#         print(kgf)
#         with open ('采集到的IP.txt','a') as h:
#             h.write(kgf)
# dailihtp()

# def dailihttps():
#     print('[+]极速爬代理IP,默认为99页')
#
#     for s in range(1,99):
#         url="http://www.xicidaili.com/wt/{}".format(s)
#         header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1 Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
#         r=requests.get(url,headers=header)
#         kl=r.content
#         lox=re.findall('(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)',kl)
#             lk in lox:
#         los=".".join(lk)
#         print(los)
#         with open('采集到的IP.txt','a') as lp:
#             lp.write(los)
#
# dailihttps()
