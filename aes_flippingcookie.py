from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes, bytes_to_long
from Crypto.Util.Padding import pad, unpad
from operator import xor
from datetime import datetime, timedelta
import requests
import os
import json
import copy

r = requests.get('http://aes.cryptohack.org/flipping_cookie/get_cookie/')
cookie_payload = json.loads(r.text)["cookie"]

iv = cookie_payload[:32]
cookie = cookie_payload[32:]

iv_new = copy.deepcopy(iv)
xor_value = (0x12 << 72 | 0x13 << 64 | 0x19 << 56 | 0x16 << 48 | 0x5e << 40) & ((0xFFFFFFFFFF << 88) >> 48)

iv_new = int(iv_new, 16) ^ xor_value 

print(hex(iv_new))

get_param = 'http://aes.cryptohack.org/flipping_cookie/check_admin/' + cookie + '/' + str(hex(iv_new))[2:] + '/'
r2 = requests.get(get_param)

print(r2.text)