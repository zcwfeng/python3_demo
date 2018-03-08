import hashlib

import codecs

header_hex = ("01000000" +
              "81cd02ab7e569e8bcd9317e2fe99f2de44d49ab2b8851ba4a308000000000000" +
              "e320b6c2fffc8d750423db8b1eb942ae710e951ed797f7affc8892b0f1fc122b" +
              "c7f5d74d" +
              "f2b9441a" +
              "42a14695")

header_bin = codecs.decode(header_hex,'hex_codec')
#header_hex.decode('hex')
print(header_bin)

hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
print(hash)

print(codecs.encode(hash,'hex_codec'))
# # '1dbd981fe6985776b644b173a4d0385ddc1aa2a829688d1e0000000000000000'
# print(hash[::-1].encode('hex_codec'))
print(codecs.encode(hash[::-1],'hex_codec'))
# # '00000000000000001e8d6829a8a21adc5d38d0a473b144b6765798e61f98bd1d'


import decimal, math
l = math.log
e = math.e
print(0x00ffff * 2**(8*(0x1d - 3)) / float(0x0404cb * 2**(8*(0x1b - 3))))
print(l(0x00ffff * 2**(8*(0x1d - 3)) / float(0x0404cb * 2**(8*(0x1b - 3)))))
print(l(0x00ffff * 2**(8*(0x1d - 3))) - l(0x0404cb * 2**(8*(0x1b - 3))))
print(l(0x00ffff) + l(2**(8*(0x1d - 3))) - l(0x0404cb) - l(2**(8*(0x1b - 3))))
print(l(0x00ffff) + (8*(0x1d - 3))*l(2) - l(0x0404cb) - (8*(0x1b - 3))*l(2))
print(l(0x00ffff / float(0x0404cb)) + (8*(0x1d - 3))*l(2) - (8*(0x1b - 3))*l(2))
print(l(0x00ffff / float(0x0404cb)) + (0x1d - 0x1b)*l(2**8))
