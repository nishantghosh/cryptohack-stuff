import requests
from Crypto.Cipher import AES
from hashlib import md5
from Crypto.Util.number import bytes_to_long, long_to_bytes

r = requests.get('https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words')
words = r.text

ct_json = {"ciphertext":"c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"}
ct = ct_json["ciphertext"]


words = words.strip().split("\n")

len_words = len(words)

for item in words:
    key = md5(item.encode()).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = bytes.fromhex(ct)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        print(str(e))
    try:    
        dec_str = long_to_bytes(int(decrypted.hex(), 16)).decode()
        if "crypto" in dec_str:
            print(dec_str)
    except:
        pass
    

