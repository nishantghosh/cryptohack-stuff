from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes, bytes_to_long
from Crypto.Util.Padding import pad, unpad
from  numpy import bitwise_xor, shape
from operator import xor
from datetime import datetime, timedelta
import requests
import os
import json
import copy

def hammingDistance(x, y):
      """
      :type x: int
      :type y: int
      :rtype: int
      """
      ans = 0
      for i in range(127,-1,-1):
         b1= x>>i&1
         b2 = y>>i&1
         ans+= not(b1==b2)
         #if not(b1==b2):
            # print(b1,b2,i)
      return ans

r = requests.get('http://aes.cryptohack.org/bean_counter/encrypt/')
enc_flag_payload = json.loads(r.text)["encrypted"]


#print(enc_flag_payload)
enc_bytes = bytearray(long_to_bytes(int(enc_flag_payload, 16)))
enc_bytes = pad(enc_bytes, 16)
len_enc = len(enc_bytes)

b1 = enc_bytes[:16]
#b2 = bytes_to_long(enc_bytes[16:32])

print("block1: ", b1)

pt_first_block = bytearray(long_to_bytes(0x89504e470d0a1a0a0000000d49484452))

print("PT first block: ", pt_first_block)

enc_key = []
for i in range(0,16):
    enc_key.append(b1[i] ^ pt_first_block[i])

print("enc key:", enc_key)

i = 0
pt = []

while i < len_enc:
    out_arr = bitwise_xor(enc_key, enc_bytes[i:i+16])
    pt.append(list(out_arr))
    i = i+16

pt = [item for sublist in pt for item in sublist]
#print(pt)

with open('flag.png', 'wb+') as f:
    for item in pt:
        f.write(long_to_bytes(item))

### pt_first_block = 89504e470d0a1a0a0000000d49484452