# coding=utf-8
import base64
encodestr = base64.b64encode(b'weiyameng123@gmail.com|weiyameng(1)')
print(encodestr)


decodestr = base64.b64decode(encodestr)
print(str(decodestr,'utf-8'))


print(base64.b64encode(b'+/binary\x00string'))
print(base64.b64decode(b'Ky9iaW5hcnkAc3RyaW5n'))
