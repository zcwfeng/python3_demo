from scapy3k.all import *
def packet_callbacke(packet):
    print(packet.show())

sniff(prn=packet_callbacke,count=1)
