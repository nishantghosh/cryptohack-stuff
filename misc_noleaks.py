from pwn import * 
import base64
import os 
import json 

req = json.dumps({"msg":"request"})

not_candidates = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[],
8:[], 9:[], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[],
18:[], 19:[]}

i = 0

while i < 256*7:
    try:
        conn = remote('socket.cryptohack.org', 13370, timeout=10)
        conn.send(req)
        payload = conn.recvlinesS(2)
        enc = json.loads(payload[1])
        print("Received enc: {}".format(enc))
        if "ciphertext" in enc:
            enc = base64.b64decode(enc["ciphertext"])
            for j in range(0,20):
                not_candidates[j].append(enc[j])
        else:
            pass
        i = i+1
    except:
        break
        #pass

for key in not_candidates:
    not_candidates[key] = list(dict.fromkeys(not_candidates[key]))
    print("not_candidates[{}]:{}".format(key, len(not_candidates[key])))

#print(not_candidates)

candidates = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[],
8:[], 9:[], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[],
18:[], 19:[]}

for key in not_candidates:
    for k in range(256):
        if k not in not_candidates[key]:
            try:
                candidates[key].append(chr(k))
            except:
                pass

print(candidates)


