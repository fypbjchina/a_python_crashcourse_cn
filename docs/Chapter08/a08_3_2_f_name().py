# a08_3_2_f_name().py
# 定义函数name(): 实参可选，形参位于末尾，默认为空，如mid_name

def name(first_name, last_name, mid_name=''):
    """返回格式为first_name.mid_name.last_name的名字"""
    if mid_name:
        full_name = f"{first_name}.{mid_name}.{last_name}"
    else:
        full_name = f"{first_name}.{last_name}"
    return full_name.title()

friend_name_01 = name('3', 'zhang') # 无mid_name, 默认形参为空
friend_name_02 = name('4', 'li', '1') # 有mid_name, 替换默认形参

print(friend_name_01)
print(friend_name_02)