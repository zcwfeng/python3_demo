import sys
from scapy3k.all import sr1,IP,ICMP

p=sr1(IP(dst=sys.argv[1])/ICMP())
if p:
    p.show()
# lsc()
# p = IP('www.somesite.ex') / TCP(80) / Raw(b'Some raw bytes')
# p = Ether()/IP()/IP()/UDP()

# # to see packet content as bytes use bytes(p) not str(p)
# sr1(p)



# import sys
# from scapy.all import sr1,IP,ICMP
#
# p=sr1(IP(dst=sys.argv[1])/ICMP())
# if p:
#     p.show()


# if __name__=="__main__":
#     main()
