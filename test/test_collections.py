
test = False

if(test):
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




# from sortedcontainers import SortedList
# sl = SortedList(['e', 'a', 'c', 'd', 'b'])
#
# print(sl)

# from dateutil import parser
# dt = parser.parse("Aug 28 2015 12:00AM")
# print(dt)
#
# import time
# start = time.clock()
# for i in range(10000):
#     print(i)
# end = time.clock()
# print('different is %6.3f' % (end - start))


delimiter = ',#'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))

a = []
for i in range(10):
    a.append([])


a = ['one', 'two', 'three']
for i in a[::-1]:
    print(i)
import random

#生成 10 到 20 之间的随机数
print(random.uniform(10, 20))

L = [1,2,3,4,5]
s1 = ','.join(str(n) for n in L)
print(s1)
print('#'.join(L.__str__()))
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(bcolors.OKGREEN + "警告的颜色字体?" + bcolors.ENDC)



