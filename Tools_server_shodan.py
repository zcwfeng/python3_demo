import optparse
import shodan
import requests
def main():
    usage='[usage: -j Type what you want]' \
      '        [-i IP to search]' \
      '        [-s Todays camera equipment]'
    parser=optparse.OptionParser(usage)
    parser.add_option('-j',dest='jost',help='Type what you want')
    parser.add_option('-i',dest='host',help='IP to search')
    parser.add_option('-s',action='store_true',dest='query',help='Todays camera equipment')
    (options,args)=parser.parse_args()
    if options.jost:
        jost=options.jost
        Jost(jost)
    elif options.host:
        host=options.host
        Host(host)
    elif options.query:
        query()
    else:
        parser.print_help()
        exit()

def Jost(jost):
    SHODAN_API_KEY='ZmgQ9FZf1rnRuR0MLhT5SXw0xBE8LDLc'
    api=shodan.Shodan(SHODAN_API_KEY)
    try:
        result=api.search('{}'.format(jost))
        print('[*]Results found:{}'.format(result['total']))
        for x in result['matches']:
            print('IP{}'.format(x['ip_str']))
            print(x['data'])
            with open('shodan.txt','a') as p:
                p.write(x['ip_str']+'\n')
                p.write(x['data']+'\n')
    except shodan.APIError as e:
        print('[-]Error:',e)

def Host(host):
    SHODAN_API_KEY='ZmgQ9FZf1rnRuR0MLhT5SXw0xBE8LDLc'
    try:
      api=shodan.Shodan(SHODAN_API_KEY)
      hx=api.host('{}'.format(host))
      print("IP:{}".format(hx['ip_str']))
      print('Organization:{}'.format(hx.get('org','n/a')))
      print('Operating System:{}'.format(hx.get('os','n/a')))
      for item in hx['data']:
          print("Port:{}".format(hx['port']))
          print('Banner:{}'.format(hx['data']))
    except shodan.APIError as g:
        print('[-]Error:',g)

def query():
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    url = "https://api.shodan.io/shodan/query?key=ZmgQ9FZf1rnRuR0MLhT5SXw0xBE8LDLc"
    r = requests.get(url, headers=header)
    sd = r.json()
    sg = sd['matches'][0:]
    for b in sg:
        print("描述:", b['description'])
        print('标签:', b['tags'])
        print('时间戳:', b['timestamp'])
        print('标题:', b['title'])
        print('服务:', b['query'])
        print('---------------------------------')

if __name__ == '__main__':
    main()
