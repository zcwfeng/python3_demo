import requests
import optparse
import json

def main():
    usage='usage:[-i IP query]' \
      '      [-m National wifi lat]' \
      '      [-l National wifi lon]' \
      '      [-x Daily News]' \
      '      [-t Info querry]'


    parser=optparse.OptionParser(usage)
    parser.add_option('-i',dest='ip',help='ip to query')
    parser.add_option('-m',dest='wifi',help='National wifi lat')


    parser.add_option('-l',dest='wifilon',help='National wifi lon')
    parser.add_option('-x',action='store_true',dest='Daily',help='Daily News')
    parser.add_option('-t',dest='info',help='info to query')
    (options,args)=parser.parse_args()
    if options.ip:
        ipquery=options.ip
        Ipquery(ipquery)
    elif options.wifi and options.wifilon:
        wifi=options.wifi
        wifilon=options.wifilon
        Wifi(wifi,wifilon)
    elif options.Daily:
        Daily()
    elif options.info:
        info=options.info
        Info(info)
    else:
        parser.print_help()
        exit()
def Ipquery(ipquery):
    url="http://api.avatardata.cn/IpLookUp/LookUp?key=6a4c1df4ba10453da7ee1d50165bfd08&ip={}".format(ipquery)
    header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    r=requests.get(url,headers=header)
    sdw=r.content.decode('utf-8')
    lks=json.loads(sdw)
    print('[*]ip',ipquery)
    print('[*]area:',lks['result']['area'])
    print('[*]location:',lks['result']['location'])

def Wifi(wifi,wifilon):
    url = "http://api.avatardata.cn/Wifi/QueryByRegion?key=你的key&lon={}&lat={}&r=3000&type=1".format(wifi,wifilon)
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    r = requests.get(url, headers=header)
    sds = r.json()


    poswe = sds['result']['data'][0:]


    for k in poswe:
        print("名字:", k['name'], "详细位置:", k['intro'], "地址:", k['address'], "纬度:", k['google_lat'], "经度:",k['google_lon'], "城市:", k['city'])
def Daily():
    url = "http://api.avatardata.cn/TouTiao/Query?key=你的key&type=top"
    header = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    r = requests.get(url, headers=header)
    sds = r.json()
    poswe = sds['result']['data'][0:]
    for k in poswe:
        print("标题:", k['title'], "日期:", k['date'], "网站来源:", k['author_name'], "新闻url:", k['url'])
def Info(info):
    url = "http://api.avatardata.cn/Weather/Query?key=你的key={}".format(info)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    r = requests.get(url, headers=header)
    sds = r.json()
    print('-------------今天天气-----------------')
    print("风度:", sds['result']['realtime']['wind']['direct'], "风力:", sds['result']['realtime']['wind']['power'])
    print("天气:", sds['result']['realtime']['weather']['info'], "温度:",
      sds['result']['realtime']['weather']['temperature'])


    print("时间:", sds['result']['realtime']['date'], "地点:", sds['result']['realtime']['city_name'], "农历:",


    sds['result']['realtime']['moon'])


    print("空调:", sds['result']['life']['info']['kongtiao'], "运动:", sds['result']['life']['info']['yundong'])
    print("紫外线:", sds['result']['life']['info']['ziwaixian'], "感冒:", sds['result']['life']['info']['ganmao'])
    print('洗车:', sds['result']['life']['info']['xiche'], "污染:", sds['result']['life']['info']['wuran'])
    print('穿衣:', sds['result']['life']['info']['chuanyi'])
    print('---------------未来几天-----------------')
    lijs = sds['result']['weather'][0:]
    for b in lijs:
        print("日期:", b['date'], "星期几:", b['week'], "农历:", b['nongli'], "早上天气:", b['info']['dawn'], "中午天气:",
              b['info']['day'], "晚上天气:", b['info']['night'])


if __name__ == '__main__':
    main()
