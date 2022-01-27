from Crypto.Util.number import long_to_bytes, bytes_to_long

encoded = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
encoded_int = int(encoded, 16)
str= long_to_bytes(encoded_int).decode()

list_str = [ord(c) for c in str]
byte = 0


while byte <= 255:
    decoded = []
    for item in list_str:
        decoded.append(chr(item ^ byte))
    decoded_str = "".join(decoded)
    if "crypto" in decoded_str:
        print(decoded_str)
    byte = byte+1