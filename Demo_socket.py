# import socket
# mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#like file open
# #AF_INET refer i'm make an internet socket
# #STREAM refer i'm make an stream socket
# mysock.connect(('www.baidu.com',80))
# #在我们这个程序和www.py4inf.com的80端口间建立一个Sockets
# toSend='GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n'
# mysock.send(toSend.encode('ascii'))
# while True:
#     data = mysock.recv(65)#65是buf长度，此处用来设置显示数据时的长度
#     if(len(data)<1):
#         break
#     print(data)
# mysock.close()

# import urllib.request
# fhand=urllib.request.urlopen('http://www.py4inf.com/code/romeo.txt')
# for line in fhand:
#     print(line.strip())

#
# import urllib.request
# fhand=urllib.request.urlopen('http://www.py4inf.com/code/romeo.txt')
# counts=dict()
# for line in fhand:
#     words=line.split()
# for word in words:
#     counts[word]=counts.get(word,0)+1
# print(counts)


# import urllib.request
# fhand=urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
# for line in fhand:
#     print(line.strip())

import urllib.request
from bs4 import BeautifulSoup
url = input('Enter - ')
html = urllib.request.urlopen(url).read()
# soup=BeautifulSoup(html,"html.parser")
soup=BeautifulSoup(html,"lxml")

tags = soup('a')
for tag in tags:
    print(tag.get('href',None))
