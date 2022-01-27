from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes, bytes_to_long
from Crypto.Util.Padding import pad, unpad
from  numpy import bitwise_xor, shape
from operator import xor
import requests
import os
import json
import copy
from zlib import compress, decompress
import binascii

i = 0
# pt_bytes = bytes.fromhex(pt)
# print(pt_bytes, len(pt_bytes))

# pt_compress = compress(pt_bytes)
# print(pt_compress, len(pt_compress))
for i in range(65536):
    pt = binascii.hexlify(bytes([i]))
    print(pt.decode())
    get_param = 'http://aes.cryptohack.org/ctrime/encrypt/' + pt.decode() + '/'
    r = requests.get(get_param)

    ct = json.loads(r.text)["ciphertext"]

    ct = bytes.fromhex(ct)
    len_ct = len(ct)

    if len_ct < 33:
        print("PT: {}, CT: {}, len_ct: {}".format(pt, ct, len_ct))
# get_param = 'http://aes.cryptohack.org/ctrime/encrypt/' + pt + '/'
# r = requests.get(get_param)

# ct = json.loads(r.text)["ciphertext"]

# ct = bytes.fromhex(ct)

#print("CT: {}, len: {}".format(ct, len(ct)))
