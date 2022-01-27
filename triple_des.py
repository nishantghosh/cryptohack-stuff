from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad
from Crypto.Util.number import long_to_bytes, bytes_to_long
import requests
import json
import os

IV = os.urandom(8)
#IV = 1
target_ct = "588f6a4e659de8a4"

def xor(a, b):
    # xor 2 bytestrings, repeating the 2nd one if necessary
    return bytes(x ^ y for x,y in zip(a, b * (1 + len(a) // len(b))))

def encrypt(key, plaintext):
    try:
        key = bytes.fromhex(key)
        plaintext = bytes.fromhex(plaintext)
        plaintext_plus_iv = xor(plaintext, bytes(IV))

        #print("pt after xor: ", hex(plaintext_plus_iv))

        cipher = DES3.new(key, DES3.MODE_ECB)
        ciphertext = cipher.encrypt(plaintext_plus_iv)
        ciphertext_plus_iv = xor(ciphertext, bytes(IV))
        return ciphertext_plus_iv
        
    except ValueError as e:
        return {"error": str(e)}

def decrypt(key, ciphertext):
    try:
        key = bytes.fromhex(key)
        ct_minus_iv = xor(ciphertext, IV)
        cipher = DES3.new(key, DES3.MODE_ECB)
        plaintext = cipher.decrypt(ct_minus_iv)
        pt_minus_iv = xor(plaintext, IV)

        pt = pt_minus_iv.hex()
        return pt
    except ValueError as e:
        return {"error": str(e)}
        

#key_in = "deadbeefcafebabe0000000000000000deadbeefcafebabe"
key_in = "FEFEFEFEFEFEFEFE1F1F1F1F0E0E0E0EFEFEFEFEFEFEFEFE"
pt_in = "FDFDFDFDFDFDFDFD"#FDFDFDFDFDFDFDFDFDFDFDFDFDFDFDFDFDFDFDFDFDFDFDFDFDFDFDFDFDFDFDFD"

# getparam_encrypt = "http://aes.cryptohack.org/triple_des/encrypt/" + key_in + '/' + pt_in + '/'
# getparam_flag = "http://aes.cryptohack.org/triple_des/encrypt_flag/" + key_in + '/'

# r = requests.get(getparam_encrypt)

# ct = json.loads(r.text)["ciphertext"]

#print("IV: ", IV)
ct = encrypt(key_in, pt_in)

# while(ct.hex() != target_ct):
#     ct = encrypt(key_in, pt_in)
#     IV = IV+1

pt = encrypt(key_in, ct.hex())
# print("Done!")
# print("CT: {}, IV: {}".format(ct.hex(), IV))

print("ct: {}, pt: {}".format(ct.hex(), pt.hex()))
#target_ct = "588f6a4e659de8a4"


