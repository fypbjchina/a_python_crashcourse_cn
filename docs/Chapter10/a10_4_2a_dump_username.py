# a10_4_2a_dump_username.py
# json.dump()存储用户名

import json

# 用户输入用户名或名字
print("Please enter your username or your name:")
username = input("Login:\t")

filename = 'a10_4_2_usernames.json'
with open(filename, 'r+') as f:
    json.dump(username, f) # 函数dump()
    print(f"Welcome to login Python-Beginner, {username}!")
    print(f.read())