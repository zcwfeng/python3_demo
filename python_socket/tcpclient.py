# coding=utf-8
import socket
# 23.99.110.21
# tgtHost = input('请输入主机:')
# tgtPort = int(input('请输入你要访问的端口:'))

tgtHost = "23.99.110.21"
tgtPort = 80

c_sock =  socket(socket.AF_INET,socket.SOCK_STREAM)
#TCP:SOCK_STREAM
#UDP:AF_INET

c_sock.connect(tgtHost,tgtPort)

c_sock.send('123'.encode())
res = c_sock.recv(100)
print('Server:',res.decode())
