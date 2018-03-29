scrapy-itzhaopin
================
* 安装Scrapy

* 进入scrapy-itzhaopin/itzhaopin

> srapy craw tencent

* 等待爬去结束,会得到一个tencent.json 文件(如果规则变了,请自行用xpath语法和css规则更改)

* 执行文件json2sql 生成sql批处理脚本

* 确认本地安装了Mysql数据库

* 创建数据库itzhaopin,创建表tencent

* 推荐一个mac电脑端的mysql客户端非常小,非常好用

> sequel pro (现在是免费的非常好用)

* 执行cmd_mysql.py 批量插入数据库表数据
