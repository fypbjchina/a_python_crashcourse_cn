# a08_4_f_welcome(names).py
# 定义函数welcome(names): 传递列表

def welcome(names):
    """问候列表中的每一位"""
    for name in names:
        print(f"Hello, {name.title()}, welcome to join us!")

name_list = ['3.zhang', '4.li', '5.wang']
welcome(name_list)