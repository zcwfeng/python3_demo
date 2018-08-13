# coding=utf-8
import nmap
# 23.99.110.215
# filter port
# close open filtered
tgtHost = '23.99.110.215'
tgtPorts = range(20,65536)
nmScan = nmap.PortScanner()
for tgtPort in tgtPorts :
    nmScan.scan(tgtHost,str(tgtPort))
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print('port[%s] ,state [%s]:' % (str(tgtPort),state))


# print(nmap.__file__)
