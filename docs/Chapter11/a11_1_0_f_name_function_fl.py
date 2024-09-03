# a11_1_0_f_name_function_fl.py
# 函数get_formatted_name() 将名和姓合并成姓名

def get_formatted_name(first, last):
    """生成整洁的姓名。"""
    full_name = f"{first} {last}"
    return full_name.title()