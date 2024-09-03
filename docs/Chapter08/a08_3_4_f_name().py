# a08_3_4_f_name().py
# 结合使用函数和while循环

def name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name}.{last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name:\t")
    if f_name == 'q':
        break
    
    l_name = input("Last name:\t")
    if l_name == 'q':
        break
    
    formatted_name = name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")