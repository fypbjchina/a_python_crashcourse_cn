# a08_2_3_f_friend().py
# 定义函数friend() - 默认值

def friend(name, time, location='beijing', country='china'):
    """显示最初认识朋友时的信息"""
    print(f"Friend Info.:")
    print(f"{name.title()}\t\t{time}\t{location.title()} @ {country.upper()}\n")

friend(name='zhang 3', time=20040401) # 使用形参默认值
friend(time=20190801, name='li 4', country='germany', location='horb') # 实参替换默认值，关键字实参
friend('wang 5', 20220801, 'rottenburg', 'germany') # 实参替换默认值，位置实参