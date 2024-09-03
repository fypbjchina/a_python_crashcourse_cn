# a08_2_2_f_friend().py
# 定义函数friend() - 关键字实参

def friend(name, time, location, country):
    """显示最初认识朋友时的信息"""
    print(f"Friend Info.:")
    print(f"{name.title()}\t\t{time}\t{location.title()} @ {country.upper()}\n")

friend(name='zhang 3', time=20040401, location='beijing', country='china')
friend(time=20190801, name='li 4', country='germany', location='horb') # 打乱位置顺序，名称值对正确，结果正确
friend(name='wang 5', time=20220801, location='rottenburg', country='germany')