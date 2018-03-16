#-*- coding:utf-8 -*-
import urllib.request

html=urllib.request.urlopen("http://movie.douban.com/chart").read()
print(html)
