from Crypto.Util.number import long_to_bytes, bytes_to_long

encoded = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
encoded_int = int(encoded, 16)
str= long_to_bytes(encoded_int).decode()

list_str = [ord(c) for c in str]
byte = 0
encoded_len = len(list_str)

my_key = "myXORkey"
my_key_list = [ord(c) for c in my_key]
xor_key_list = []
my_key_len = len(my_key_list)

for i in range(my_key_len * (int(encoded_len/my_key_len) + 1) - encoded_len):
    list_str.append(0)

for i in range(int(encoded_len/my_key_len)+1):
    xor_key_list = xor_key_list + my_key_list

xor_key_len = len(xor_key_list)
decoded = []

for i in range(xor_key_len):
    decoded.append(chr(list_str[i] ^ xor_key_list[i]))
decoded_str = "".join(decoded)

print(decoded_str)
#flag = False
#print(list_str)

# while byte <= 255:
#     decoded = []
#     for item in list_str:
#         decoded.append(chr(item ^ byte))
#     decoded_str = "".join(decoded)
#     if "{" in decoded_str:
#         print(decoded_str)
#         print(byte)
#         print("\n")
#         #flag = True
#     byte = byte+1

# while byte <= 255:

#     if 'c' in (chr(list_str[0] ^ byte)):
#         print("c", byte, chr(byte))
#     if 'r' in (chr(list_str[1] ^ byte)):
#         print("r", byte, chr(byte))
#     if 'y' in (chr(list_str[2] ^ byte)):
#         print("y", byte, chr(byte))
#     if 'p' in (chr(list_str[3] ^ byte)):
#         print("p", byte, chr(byte))
#     if 't' in (chr(list_str[4] ^ byte)):
#         print("t", byte, chr(byte))
#     if 'o' in (chr(list_str[5] ^ byte)):
#         print("o",byte, chr(byte))
#     if '{' in (chr(list_str[6] ^ byte)):
#         print("{", byte, chr(byte))
#     # if 'F' in (chr(list_str[7] ^ byte)):
#     #     print("F", byte, chr(byte))
#     # if 'L' in (chr(list_str[8] ^ byte)):
#     #     print("L", byte, chr(byte))
#     # if 'A' in (chr(list_str[9] ^ byte)):
#     #     print("A", byte, chr(byte))
#     # if 'G' in (chr(list_str[10] ^ byte)):
#     #     print("G", byte, chr(byte))
#     if '}' in (chr(list_str[7] ^ byte)):
#         print("}", byte, chr(byte))
#     byte = byte+1

