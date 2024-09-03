# a10_4_2c_remember_username.py
# json.load(), dump()加载/存储用户名
# try-except处理异常

import json
# 如果以前存储了用户名，就加载它。
# 否则，提示用户输入用户名并存储它。

filename = 'a10_4_2_username.json'
try:
    with open(filename) as f:
        username = json.load(f) # 函数load()
except FileNotFoundError:
    print("Please enter your username or your name:")
    username = input("Login:\t")    
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"Welcome to login Python-Beginner, {username}!")
else:
    print(f"Welcome back, {username}!")