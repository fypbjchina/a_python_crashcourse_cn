# a11_1_3_f_name_function_fml.py
# 函数get_fml_name() 将名和姓合并成姓名

def get_fml_name(first, middle, last):
    """生成整洁的姓名。"""
    full_name = f"{first} {middle} {last}"
    return full_name.title()