# a10_4_3_remember_me.py
# 重构load_username, dump_username, greet_user

import json

def load_username():
    """如果存储了用户名，就获取它"""
    filename = 'a10_4_2_username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
def dump_username():
    """提示用户输入用户名"""
    print("Please enter your username or your name:")
    username = input("Login:\t")
    
    filename = 'a10_4_2_username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    
    return username

def greet_user():
    """问候用户，并指出其名字"""
    username = load_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = dump_username()
        print(f"Welcome to login Python-Beginner, {username}!")

greet_user()