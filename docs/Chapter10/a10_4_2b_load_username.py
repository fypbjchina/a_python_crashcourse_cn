# a10_4_2b_load_username.py
# json.load()加载用户名

import json

filename = 'a10_4_2_usernames.json'
with open(filename) as f:
    username = json.load(f) # 函数load()
    print(f"Welcome to login Python-Beginner, {username}!")