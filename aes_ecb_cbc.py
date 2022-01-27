from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes, bytes_to_long
from Crypto.Util.Padding import pad, unpad
from operator import xor
import requests
import json

cbc_param = 'http://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/'
r = requests.get(cbc_param)

ct_payload = json.loads(r.text)["ciphertext"]
iv = ct_payload[:32]
ct = ct_payload[32:]

ecb_param = 'http://aes.cryptohack.org/ecbcbcwtf/decrypt/' + ct + '/'
r2 = requests.get(ecb_param)

pt_payload = json.loads(r2.text)["plaintext"]

pt_1 = xor(int(iv, 16), int(pt_payload[:32], 16))
pt_2 = xor(int(ct[:32], 16), int(pt_payload[32:], 16))

print(long_to_bytes(pt_1).decode(), long_to_bytes(pt_2).decode())



