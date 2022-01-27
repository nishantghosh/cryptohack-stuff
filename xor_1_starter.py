encoded = "label"
encoded_ascii = [ord(c) for c in encoded]
decoded = []
for item in encoded_ascii:
    res = item ^ 13 
    decoded.append(chr(res))

print("".join(decoded))
 