hex_data = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
#bytearray_hex = bytearray.fromhex(hex_data)
bytes_hex = bytes.fromhex(hex_data)
print(bytes_hex)

# list_chr = []
# i = len(hex_data)
# while i > 0:
#     list_chr.append(chr(int((hex_data[i-2:i]), 16)))
#     i = i-2

# str = "".join(list_chr)
# str = str[::-1]

# print(str)
