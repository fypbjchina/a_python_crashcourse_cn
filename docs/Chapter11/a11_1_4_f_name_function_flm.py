# a11_1_4_f_name_function_flm.py
# 函数get_flm_name() 将名和姓合并成姓名

def get_flm_name(first, last, middle=''):
    """生成整洁的姓名。"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()