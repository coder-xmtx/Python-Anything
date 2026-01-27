# 加密字符

import random
import string

# 导入一些字符（大小写字母、数字、标点符号等）
chars = string.ascii_letters + string.digits + string.punctuation + " "
chars = list(chars)
key = chars.copy()

# 打乱字符顺序
random.shuffle(key)

# 加密函数
plain_text = input("Please enter the text you want to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original text: {plain_text}")
print(f"Encrypted text: {cipher_text}")
