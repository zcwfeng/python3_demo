from dnsknife.scanner import Scanner
import dnsknife
import optparse
import sys
def main():
    usage="[-i Fast query] " \
      "[-d DNS domain transmission vulnerability detection]"
    parser=optparse.OptionParser(usage)
    parser.add_option('-i',dest='Fastquery',help='Quickly check some dns records')
    parser.add_option('-d',dest='detection',help='Detects possible DNS transmission vulnerabilities')
    (options,parser)=parser.parse_args()
    if options.Fastquery :
        Fastquery=options.Fastquery
        query(Fastquery)
    elif  options.detection :
        detection=options.detection
        vulnerability(detection)
    else:
        sys.exit()
def query(Fastquery):
    print('--------mx record--------')

    try:
        dns=dnsknife.Checker(Fastquery).mx()
        for x in dns:
          print(x)
    except(Exception, c):
        print('[-]wrong reason:',c)
    print('--------txt record--------')
    try:
        dnstxt=dnsknife.Checker(Fastquery).txt()
        print(dnstxt)
    except(Exception , g):
        print('[-]wrong reason:',g)
    try:
        print('--------spf record------')
        dnsspf=dnsknife.Checker(Fastquery).spf()
        print(dnsspf)
    except(Exception , l):
        print('[-]wrong reason:',l)


def vulnerability(detection):
    print('--------DNS transmission vulnerability detection-----------')
    try:
      dnschuan=Scanner(detection).scan()
      for list in dnschuan:
          print(list)
    except(Exception , p):
        print('[-]Wrong reason:',p)
if __name__ == '__main__':
    main()
