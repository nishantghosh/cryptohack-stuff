from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes, bytes_to_long
from Crypto.Util.Padding import pad, unpad
from operator import xor
from datetime import datetime, timedelta
import requests
import os
import json
import copy

r = requests.get('http://aes.cryptohack.org/symmetry/encrypt_flag/')
enc_flag_payload = json.loads(r.text)["ciphertext"]
iv = enc_flag_payload[:32]
enc_flag = enc_flag_payload[32:]

get_param = 'http://aes.cryptohack.org/symmetry/encrypt/' + enc_flag + '/' + iv + '/'
r = requests.get(get_param)

flag = long_to_bytes(int(json.loads(r.text)["ciphertext"], 16))

print(flag)