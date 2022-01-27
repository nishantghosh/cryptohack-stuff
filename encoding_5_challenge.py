from Crypto.Util.number import bytes_to_long, long_to_bytes
import ast
import json
from pwn import *
import utils
import base64
import codecs
import random

conn = remote('socket.cryptohack.org', 13377)
flag = False
i=0

while flag != True:
    req_in = conn.recvline()
    req_in = req_in.decode('utf-8')
    print("iter{}:{}".format(i, req_in))
    my_data = ast.literal_eval(req_in)

    if "flag" in my_data:
        print(my_data["flag"])
        flag = True
    else:
        try:
            ct_type = my_data['type']
            pt_load = {}
            ct = my_data['encoded']
            pt_load['type'] = ct_type
            if ct_type == 'hex':
                bytes_data = bytes.fromhex(ct)
                pt_load['decoded'] = bytes_data.decode('utf-8')
                print(pt_load)
            elif ct_type == 'base64':
                b64_data = base64.b64decode(ct.encode()).decode()
                pt_load['decoded'] = b64_data
                print(pt_load)
            elif ct_type == 'utf-8':
                seq = []
                for item in ct:
                    seq.append(chr(item))
                str = "".join(seq)
                pt_load['decoded'] = str
                print(pt_load)
            elif ct_type == 'rot13':
                pt_load['decoded'] = codecs.decode(ct, 'rot13')
                print(pt_load)
            elif ct_type == 'bigint':
                pt_load['decoded'] = long_to_bytes(int(ct, 16)).decode()
                print(pt_load)
            else:
                conn.close()
        except:
            print("Error")

    pt_json = json.dumps(pt_load).encode('utf-8')
    conn.send(pt_json)
    i = i+1
