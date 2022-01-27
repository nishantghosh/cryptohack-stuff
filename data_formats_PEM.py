def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

modulus = "00:ce:f2:83:b7:e1:0e:f8:0e:a8:13:52:c8:b5:2b:a7:91:62:7c:bc:de:93:81:cb:bc:0a:4d:3b:ee:3a:06:0d:f1:b6:36:dc:43:e2:fc:90:c4:64:d0:9e:0a:fa:8c:42:89:b9:5c:f6:30:8c:03:71:d5:ed:14:b2:05:f8:84:97:f4:77:c0:2d:0d:f2:89:e7:4d:4b:cd:27:fd:34:75:04:d7:09:4a:5c:c8:ba:a2:e6:17:17:5d:9a:39:9f:52:f1:c5:b8:52:ef:c6:05:d1:81:ad: \
e6:83:7a:fb:a2:54:d6:fb:57:f1:39:2d:19:55:e0: \
c9:a8:50:9a:39:14:6f:a0:06:0e:80:b8:2e:77:6f: \
c4:d1:a6:9a:26:2f:5c:37:b0:a3:99:d2:7b:43:79: \
ba:af:21:ae:0b:0a:84:bd:9d:4a:81:55:96:6b:b7: \
ca:70:5a:29:9e:5f:df:72:c4:9e:73:06:c3:57:98: \
56:7e:6b:f1:88:05:09:cb:59:8d:48:fc:24:7f:96: \
21:19:0f:bc:de:0f:4d:e7:cf:11:a4:b2:cc:5e:68: \
2d:e8:a8:a6:b6:25:a7:26:ca:ad:0c:f4:65:63:80:63:c5:da:6e:57:74:32:51:da:36:ca:6a:a7:aa:e6:67:13:fb:e5:53:f8:67:eb:fb:3c:f9:cb:5d:4e:a7:d2:0b" 

priv_exp = "7c:3b:1d:53:4f:29:9b:43:c1:26:08:76:30:3c:0a: \
    95:be:17:bf:91:a5:df:2f:1c:ac:da:7c:75:a0:23: \
    6e:4f:81:e1:21:0d:27:c0:12:6f:b3:4d:80:f2:7a: \
    41:a4:d7:e4:8c:a7:c5:b0:e7:88:78:b1:9f:d0:d6: \
    c0:bf:68:30:fb:8a:44:01:b1:6d:93:8a:d5:4c:4d: \
    0b:35:68:62:05:6c:b0:55:4e:b2:ab:83:90:ad:18: \
    25:b3:1d:af:bf:2f:c0:5d:19:4f:38:c2:f2:24:20: \
    d3:21:0a:da:02:30:24:26:40:ca:e0:05:eb:85:cb: \
    c8:dc:ca:18:25:ea:74:96:d9:b1:70:c5:cb:fe:35: \
    4f:e1:9a:63:10:2b:82:f3:8d:5d:7c:25:17:35:20: \
    8b:83:a5:42:40:92:7f:89:98:48:c1:6a:5f:e7:0c: \
    e9:50:da:ff:7b:f9:f4:b7:1b:59:81:01:a5:20:48: \
    cd:30:c1:6c:b9:94:33:0b:10:59:2d:2c:95:d4:d0: \
    e5:79:f5:28:7f:f7:4a:88:26:8d:03:89:69:8c:8f: \
    7b:9a:e8:13:f3:92:46:89:3d:02:66:1c:f0:8d:9c: \
    bc:ec:9f:72:2c:f7:6d:0e:96:f1:e1:77:37:e2:9e: \
    ce:86:76:76:7c:b6:e1:df:0d:bd:2d:73:1e:d8:48:b1"

prime1 = "00:ed:fb:47:15:eb:a9:3b:c4:c2:cb:e7:12:c8:08: \
    10:27:cc:86:a8:d2:8d:2c:78:c9:72:0e:6d:e6:f6: \
    80:31:e0:e3:4f:fa:5e:ef:0f:d1:d0:85:ae:49:c0: \
    a8:00:38:8b:f7:ee:98:a9:4a:77:e1:18:1e:60:39: \
    24:b3:b3:bb:9d:ce:97:b8:00:62:f2:83:0c:8f:11: \
    98:3d:fa:dd:55:f1:f9:ce:53:62:99:2e:14:c2:5f: \
    77:6e:f7:da:ce:eb:71:9e:1c:f9:f2:f6:2f:4b:a6: \
    d0:03:de:4d:42:7e:eb:5a:4d:98:15:64:4f:ce:12: \
    55:93:1b:df:2b:a3:7f:c7:a7"

prime2 = "00:de:9d:b5:c3:5d:25:62:f1:cd:36:22:34:28:18: \
    c7:be:ba:03:33:20:7e:df:db:c3:f2:64:8e:6d:14: \
    10:b8:91:49:74:a5:ae:32:af:a8:e4:ea:e4:0b:42: \
    ad:a5:86:7e:1b:0e:33:2f:d0:d0:a2:c8:a9:de:1a: \
    db:ed:bd:81:f9:ba:b4:c8:fe:c8:ce:3e:66:01:55: \
    e2:cd:04:c6:92:5b:93:fd:88:af:be:05:dc:c5:52: \
    a8:36:e3:53:a9:31:20:9b:23:a1:3e:7e:b0:f8:fa: \
    91:9c:44:ac:48:5c:e3:7d:6a:da:85:30:ab:56:89: \
    9c:66:69:d4:4c:58:74:ae:fd"


priv_exp = priv_exp.strip("\n").replace(":", "").replace(" ","")
modulus = modulus.strip("\n").replace(":", "").replace(" ","")
prime1 = prime1.strip("\n").replace(":", "").replace(" ","")
prime2 = prime2.strip("\n").replace(":", "").replace(" ","")

priv_exp = int(priv_exp, 16)
modulus = int(modulus, 16)
p = int(prime1, 16)
q = int(prime2, 16)
e = 0x010001
phi = (p-1) * (q-1)

d = modinv(e, phi)
print(d)
