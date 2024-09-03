# a08_3_1_f_name().py
# 定义函数name(): return语句 - 返回值

def name(first_name, last_name):
    """返回格式为first_name.last_name的名字"""
    full_name = f"{first_name}.{last_name}"
    print(full_name)
   # return full_name.title()

friend_name = name('3', 'zhang')
print(friend_name)