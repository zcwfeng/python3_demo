import optparse

def main():
    usage='[usage: -z Type what you want]' \
      '        [-c IP to search]' \
      '        [-w Todays camera equipment]'
    parser=optparse.OptionParser(usage)
    parser.add_option('-z',dest='jost',help='帅哥大帅哥')
    parser.add_option('-c',dest='host',help='IP to search')
    parser.add_option('-w',action='store_true',dest='query',help='Todays camera equipment')
    (options,args)=parser.parse_args()
    if options.jost:
        jost=options.jost
        z(jost)
    elif options.host:
        host=options.host
        c(host)
    elif options.query:
        w()
    else:
        parser.print_help()
        exit()

def z(jost):
    print(jost)

def c(host):
    print(host)

def w():
    print("zcw")


if __name__ == '__main__':
    main()
