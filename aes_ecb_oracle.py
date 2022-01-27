from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes, bytes_to_long
from Crypto.Util.Padding import pad, unpad
import requests
import json

input = "A" * 8 
input = hex(bytes_to_long(input.encode()))
input = str(input)[2:]

get_param = 'http://aes.cryptohack.org/ecb_oracle/encrypt/' + input + '/'

r = requests.get(get_param)
ct = json.loads(r.text)["ciphertext"]
len_ct = len(ct)

ct_list = []
for byte in range(256):
    new_input = input + "63727970746f7b70336e3675316e355f683437335f3363" + f"{byte:0{2}x}"
    new_param = 'http://aes.cryptohack.org/ecb_oracle/encrypt/' + new_input + '/'
    r2 = requests.get(new_param)
    ct2 = json.loads(r2.text)["ciphertext"]
    ct_list.append(ct2)
    if ct[:64] in ct2:
        print(byte)
