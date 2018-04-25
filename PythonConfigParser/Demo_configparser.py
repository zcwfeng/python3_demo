try:
    import ConfigParser
except ImportError:
    import configparser as ConfigParser

cf = ConfigParser.ConfigParser()
cf.read("test.conf")
secs = cf.sections()
print("sections,",secs)

opts = cf.options('a')
print("options a:",opts)

kvs = cf.items('a')
print('sec_a:',kvs)

kvs1 = cf.items('others')
print('sec_others:',kvs1)

str_val = cf.get('a', 'a_key1')     # 返回a章节里面key为a_key1的值，返回为string类型
int_val = cf.getint('a', 'a_key2')  # 返回_a章节里面key为a_key2的值，返回为int类型
print("value for a's a_key1:", str_val)
print("value for a's a_key2:", int_val)


#  写测试
# cf.set("b", "b_key3", "new-$r")     # 章节a里面添加一个key为b_key3，值为new-$r，如果key存在就更新key的值
# cf.set("b", "b_newkey", "new-value")    # 章节b里面添加一个key为b_newkey，值为new-value，key存在就更新key的值
# cf.add_section('a_new_section')     # 新建一个章节a_new_section
# cf.set('a_new_section', 'new_key', 'new_value')     # 章节a_new_section里面新建一个key为new_key，值为new_value
# cf.write(open("test.conf", "w"))    # 把修改写入到文件test.conf中
# cf.read("test.config")
# print("sections after write,",cf.sections())
# 写测试end



