from pwn import *
import json
from Crypto.Util.number import long_to_bytes

r = remote('socket.cryptohack.org', 13372)
r.recvline()

flag = False

while flag != True: 
    enc_req = {"option":"encrypt_data", "input_data":"0"*64}
    flag_req = {"option":"get_flag"}
    r.send(json.dumps(enc_req))
    r.send(json.dumps(flag_req))

    key = json.loads(r.recvline())["encrypted_data"]
    enc_flag = json.loads(r.recvline())["encrypted_flag"]
    #print(r.recvuntil('', drop=True))

    len_flag = len(enc_flag)

    flag = int(key[:len_flag], 16) ^ int(enc_flag, 16)

    try:
        print(long_to_bytes(flag).decode())
        flag = True
    except:
        pass


