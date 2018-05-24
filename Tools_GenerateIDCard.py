import random
import time
def idcard_generator():
	""" 随机生成新的18为身份证号码 """
	ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
	LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
	t = time.localtime()[0]
	x = '%02d%02d%02d%04d%02d%02d%03d' % (random.randint(10, 99), random.randint(1, 99), random.randint(1, 99), random.randint(t - 80, t - 18), random.randint(1, 12), random.randint(1, 28), random.randint(1, 999))
	y = 0
	for i in range(17):
		y += int(x[i]) * ARR[i]
	IDCard = '%s%s' % (x, LAST[y % 11])
	# birthday = '%s-%s-%s 00:00:00' % (IDCard[6:14][0:4], IDCard[6:14][4: 6], IDCard[6:14][6:8])
	return IDCard

# 身份证简单校验正确性
def check_true(x1):
    """ 验证身份证号码是否真实号码 """
    # print('请输入身份证号码')
    # x1 = input('?')


    ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
    xlen = len(x1)
    if xlen != 18 and xlen != 15:
        return '身份证号码长度错误'


    try:
        if xlen == 18:
            x2 = x1[6:14]
            x3 = time.strptime(x2, '%Y%m%d')
            if x2 < '19000101' or x3 > time.localtime():
                return '时间错误，超过允许的时间范围'
        else:
            x2 = time.strptime(x1[6:12], '%y%m%d')
    except Exception as e:
        return '时间错误，非合法时间' + str(e)


    if xlen == 18:
        y = 0
        for i in range(17):
            y += int(x1[i]) * ARR[i]


        if LAST[y % 11] != x1[-1].upper():
            return '验证码错误'
    return 'YES'





import re
#Errors=['验证通过!','身份证号码位数不对!','身份证号码出生日期超出范围或含有非法字符!','身份证号码校验错误!','身份证地区非法!']
def checkIdcard(idcard):
    #地区校验
    Errors=["验证通过!",'身份证号码位数不对!','身份证号码出生日期超出范围或含有非法字符!','身份证号码校验错误!','身份证地区非法!']
    area={"11":"北京","12":"天津","13":"河北","14":"山西","15":"内蒙古","21":"辽宁","22":"吉林","23":"黑龙江","31":"上海","32":"江苏","33":"浙江","34":"安徽","35":"福建","36":"江西","37":"山东","41":"河南","42":"湖北","43":"湖南","44":"广东","45":"广西","46":"海南","50":"重庆","51":"四川","52":"贵州","53":"云南","54":"西藏","61":"陕西","62":"甘肃","63":"青海","64":"宁夏","65":"新疆","71":"台湾","81":"香港","82":"澳门","91":"国外"}
    idcard=str(idcard)
    idcard=idcard.strip()
    idcard_list=list(idcard)
    print(idcard_list)

    #地区校验
    if((idcard)[0:2] in area.keys()):
        print("地区--->",area.get((idcard)[0:2]))
    else:
        print('\033[1;35m',Errors[4],'\033[0m')
    #15位身份号码检测
    if(len(idcard)==15):
      if((int(idcard[6:8])+1900) % 4 == 0 or((int(idcard[6:8])+1900) % 100 == 0 and (int(idcard[6:8])+1900) % 4 == 0 )):
        erg=re.compile('[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}$')#//测试出生日期的合法性
      else:
        ereg=re.compile('[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}$')#//测试出生日期的合法性
      if(re.match(ereg,idcard)):
        print(Errors[0])
      else:
        print(Errors[2])
    #18位身份号码检测
    elif(len(idcard)==18):
      #出生日期的合法性检查
      #闰年月日:((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))
      #平年月日:((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))
      if(int(idcard[6:10]) % 4 == 0 or (int(idcard[6:10]) % 100 == 0 and int(idcard[6:10])%4 == 0 )):
        ereg=re.compile('[1-9][0-9]{5}19[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}[0-9Xx]$')#//闰年出生日期的合法性正则表达式
      else:
        ereg=re.compile('[1-9][0-9]{5}19[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}[0-9Xx]$')#//平年出生日期的合法性正则表达式
      #//测试出生日期的合法性
      if(re.match(ereg,idcard)):
        #//计算校验位
        S = (int(idcard_list[0]) + int(idcard_list[10])) * 7 + (int(idcard_list[1]) + int(idcard_list[11])) * 9 + (int(idcard_list[2]) + int(idcard_list[12])) * 10 + (int(idcard_list[3]) + int(idcard_list[13])) * 5 + (int(idcard_list[4]) + int(idcard_list[14])) * 8 + (int(idcard_list[5]) + int(idcard_list[15])) * 4 + (int(idcard_list[6]) + int(idcard_list[16])) * 2 + int(idcard_list[7]) * 1 + int(idcard_list[8]) * 6 + int(idcard_list[9]) * 3
        Y = S % 11
        M = "F"
        JYM = "10X98765432"
        M = JYM[Y]#判断校验位
        if(M == idcard_list[17]):#检测ID的校验位
          print(Errors[0])
        else:
          print(Errors[3])
      else:
        print(Errors[2])
    else:
      print(Errors[1])



# 身份证简单解析,出生年月,男/女

def simpleParse(ID):
    ID_add=ID[0:6]
    ID_birth=ID[6:14]
    ID_sex=ID[14:17]
    ID_check=ID[17]

    #ID_add是身份证中的区域代码，如果有一个行政区划代码字典，就可以用获取大致地址#

    year=ID_birth[0:4]
    moon=ID_birth[4:6]
    day=ID_birth[6:8]


    if int(ID_sex)%2==0:
      print("生日: "+year+'年'+moon+'月'+day+'日','性别：女')
    else:
      print("生日: "+year+'年'+moon+'月'+day+'日','性别：男')


def main():
    idcard = idcard_generator()
    isOk = check_true(idcard)

    checkIdcard(idcard)
    print("生成身份证IDCard:",idcard,"--->是否符合标准:",isOk)
    if(isOk):
        simpleParse(idcard)
    else:
        print("身份证非法")
    # print('\033[0;35m test \033[0m')
    # print('\033[5;32;43m test [\033[0m')
    # print('\033[1;33;44mThis is a test !\033[0m')



if __name__ == '__main__':
    main()
