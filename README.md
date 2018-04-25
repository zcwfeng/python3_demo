# python3_demo
python 基础性demo

不定期更新

# 使用地址
http://www.xicidaili.com/nt/

# 比较厉害的例子

## 第三方库 third_lib
* OpenCV demo,二维码识别
* Appium  unitest 测试用 webdriver
* bitcoinexchangefh  比特币扫描下载入库
* python-ConfigParser 客户端交互
* python-Yaml 客户端配置文件交互
* IP 扫描
* 服务其定位获取服务器信息
* Scrapy-itzhaopin  抓取腾讯的招聘信息入库,或者json文件


# 参考文章

- opencv
> http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html#face-detection

# 工具总结

> ipynb 文件很好奇,那么你用下面的方式就比较舒服了

--------------------------------------------------------------------------------


通过安装ipython 和jupyter
安装命令如下:

```
sudo pip install ipython --upgrade
sudo pip install jupyter
```
接下来只需要在终端中输入:`jupyter notebook`


> Pillow

--------------------------------------------------------------------------------

PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。PIL功能非常强大，但API却非常简单易用。
由于PIL仅支持到Python 2.7，加上年久失修，于是一群志愿者在PIL的基础上创建了兼容的版本，名字叫Pillow，支持最新Python 3.x，又加入了许多新特性，因此，我们可以直接安装使用Pillow。

pip3 install pillow

> requests

--------------------------------------------------------------------------------

Python内置的urllib模块，用于访问网络资源。但是，它用起来比较麻烦，而且，缺少很多实用的高级功能。
更好的方案是使用requests。它是一个Python第三方库，处理URL资源特别方便。

$ pip3 install requests


> chardet
--------------------------------------------------------------------------------

字符串编码一直是令人非常头疼的问题，尤其是我们在处理一些不规范的第三方网页的时候。虽然Python提供了Unicode表示的str和bytes两种数据类型，并且可以通过encode()和decode()方法转换，但是，在不知道编码的情况下，对bytes做decode()不好做。
对于未知编码的bytes，要把它转换成str，需要先“猜测”编码。猜测的方式是先收集各种编码的特征字符，根据特征字符判断，就能有很大概率“猜对”。
当然，我们肯定不能从头自己写这个检测编码的功能，这样做费时费力。chardet这个第三方库正好就派上了用场。用它来检测编码，简单易用。

$ pip3 install chardet


>  psutil
--------------------------------------------------------------------------------


用Python来编写脚本简化日常的运维工作是Python的一个重要用途。在Linux下，有许多系统命令可以让我们时刻监控系统运行的状态，如ps，top，free等等。要获取这些系统信息，Python可以通过subprocess模块调用并获取结果。但这样做显得很麻烦，尤其是要写很多解析代码。
在Python中获取系统信息的另一个好办法是使用psutil这个第三方模块。顾名思义，psutil = process and system utilities，它不仅可以通过一两行代码实现系统监控，还可以跨平台使用，支持Linux／UNIX／OSX／Windows等，是系统管理员和运维小伙伴不可或缺的必备模块。

$ pip3 install psutil


>  Web 框架 flask
--------------------------------------------------------------------------------


由于用Python开发一个Web框架十分容易，所以Python有上百个开源的Web框架。这里我们先不讨论各种Web框架的优缺点，直接选择一个比较流行的Web框架——Flask来使用。

pip3 install flask
Flask自带的Server在端口5000上监听：

> 模板
--------------------------------------------------------------------------------


和Web框架类似，Python的模板也有很多种。Flask默认支持的模板是jinja2，所以我们先直接安装jinja2：

pip3 install jinja2

>  异步IO

asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持。
asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。

>  aiohttp 框架
--------------------------------------------------------------------------------


asyncio可以实现单线程并发IO操作。如果仅用在客户端，发挥的威力不大。如果把asyncio用在服务器端，例如Web服务器，由于HTTP连接就是IO操作，因此可以用单线程+coroutine实现多用户的高并发支持。
asyncio实现了TCP、UDP、SSL等协议，aiohttp则是基于asyncio实现的HTTP框架。

pip3 install aiohttp

>  最简单的服务器
进入某个文件目录，这个目录就可以用网络访问
python 2 和 python3 略有不同
python2 命令
python -m SimpleHTTPServer 8088
python3 命令
python3 -m http.server 8888

>  Scrapy 爬虫框架
--------------------------------------------------------------------------------


已经支持到了python3
https://doc.scrapy.org/en/latest/intro/install.html#intro-install

>  virtualenv
--------------------------------------------------------------------------------

python 的隔离环境

>  Python3中的str.decode(‘hex’)
在Python2.x中经常使用str_obj.decode(‘hex’)在Python3.x中无法使用了。
在Python3.x中可以使用codecs.decode(str_obj, ‘hex_codec’)。

>  httpbin
--------------------------------------------------------------------------------

(在线测试:http://httpbin.org/)
Installing and running from PyPI
You can install httpbin as a library from PyPI and run it as a WSGI app. For example, using Gunicorn:
$ pip install httpbin
$ gunicorn httpbin:app

运行后:http://localhost:8000/

>  OpenCV
--------------------------------------------------------------------------------

https://www.pyimagesearch.com/2015/06/29/install-opencv-3-0-and-python-3-4-on-osx/

>   beautifulsoup4 解释器

--------------------------------------------------------------------------------

Beautiful Soup支持Python标准库中的HTML解析器,还支持一些第三方的解析器，如果我们不安装它，则 Python 会使用 Python默认的解析器，lxml 解析器更加强大，速度更快，推荐安装。

pip3 install beautifulsoup4

https://cuiqingcai.com/1319.html

>  html5lib 解释器

--------------------------------------------------------------------------------

另一个可供选择的解析器是纯Python实现的 html5lib , html5lib的解析方式与浏览器相同,可以选择下列方法来安装html5lib:


>  Scrapy 依赖的python库
--------------------------------------------------------------------------------


Things that are good to know
Scrapy is written in pure Python and depends on a few key Python packages (among others):

  ● lxml, an efficient XML and HTML parser

  ● parsel, an HTML/XML data extraction library written on top of lxml,

  ● w3lib, a multi-purpose helper for dealing with URLs and web page encodings

  ● twisted, an asynchronous networking framework

  ● cryptography and pyOpenSSL, to deal with various network-level security needs

>  pyPdf python-nmap pygeoip mechanize
