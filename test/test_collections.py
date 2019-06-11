i = ['a','b']
l = [1,2]

print(dict([i,l]))

#copy
a = [1, 2, 3]
b = a[:]
print(b)


import time

myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
    print(key,value)
    time.sleep(1) # 暂停 1 秒

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

# 暂停一秒
time.sleep(1)
 
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

import datetime
# 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
print(datetime.date.today().strftime('%d/%m/%Y'))
# 创建日期对象
miyazakiBirthDate = datetime.date(1941, 1, 5)

print(miyazakiBirthDate.strftime('%d/%m/%Y'))

# 日期算术运算
miyazakiBirthNextDay = miyazakiBirthDate + datetime.timedelta(days=1)

print(miyazakiBirthNextDay.strftime('%d/%m/%Y'))

# 日期替换
miyazakiFirstBirthday = miyazakiBirthDate.replace(year=miyazakiBirthDate.year + 1)

print(miyazakiFirstBirthday.strftime('%d/%m/%Y'))
