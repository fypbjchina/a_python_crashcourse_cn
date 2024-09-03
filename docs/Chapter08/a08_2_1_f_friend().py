# a08_2_1_f_friend().py
# 定义函数friend() - 位置实参

def friend(name, time, location, country):
    """显示最初认识朋友时的信息"""
    print(f"Friend Info.:")
    print(f"{name.title()}\t\t{time}\t{location.title()}  @ {country.upper()}\n")

friend('zhang 3', 20040401, 'beijing', 'china')
friend('li 4', 20190801, 'horb', 'germany')
friend('wang 5', 20220801, 'rottenburg', 'germany')