from PIL import Image, ImageChops
import numpy as np

try:
    lemur_img = Image.open('/Users/nishantghosh/workspace/ctf/cryptohack/lemur_89cf5c3a95326db302462d5e171c5bcf.png')
    flag_img = Image.open('/Users/nishantghosh/workspace/ctf/cryptohack/flag_712dffa77cdf390c98c947ee4601abec.png')
except IOError:
    pass

print("lemur image mode: ", lemur_img.mode, lemur_img.size)
print("flag image mode: ", flag_img.mode, flag_img.size)

lemur_np = np.array(lemur_img)
flag_np = np.array(flag_img)

xor_img = np.bitwise_xor(lemur_np, flag_np).astype(np.uint8)
Image.fromarray(xor_img).save('result.png')
