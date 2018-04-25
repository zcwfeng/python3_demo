try:
    import ConfigParser
except ImportError:
    import configparser as ConfigParser

cf2 = ConfigParser.RawConfigParser()
print("use RawConfigParser() read")
cf2.read("test2.conf")  # 读取配置文件内容
print(cf2.get("portal", "url"))  # 获得章节portal中key为url的值
print("use RawConfigParser() write")
cf2.set("portal", "url12", "%(host)s:%(port)s") # 章节portal中添加一个key为url12，值为%(host)s:%(port)s
print(cf2.get("portal", "url12"))   # 获得章节portal中key为url12的内容

cf3 = ConfigParser.ConfigParser()
print("use ConfigParser() read")
cf3.read("test2.conf")
print(cf3.get("portal", "url"))
print("use ConfigParser() write")
cf3.set("portal", "url12", "%(host)s:%(port)s")
print(cf3.get("portal", "url12"))

cf4 = ConfigParser.SafeConfigParser()
print("use SafeConfigParser() read")
cf4.read("test2.conf")
print(cf4.get("portal", "url"))
print("use SateConfigParser() write")
cf4.set("portal", "url2", "%(host)s:%(port)s")
print(cf4.get("portal", "url2"))
