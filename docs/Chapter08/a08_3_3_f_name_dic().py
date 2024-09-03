# a08_3_3_f_name_dic().py
# 定义函数name_dic(): return语句 - 返回字典

def name_dic(first_name, last_name, age=False):
    """返回一个字典，包含人名信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age # 有age信息，添加键值对 'age'-age 到字典
    return person 

friend_name_01 = name_dic('3', 'zhang') # 无age, 默认形参为空, None=''=False
friend_name_02 = name_dic('4', 'li', age=20) # 关键字实参age 等效 位置实参age

print(friend_name_01)
print(friend_name_02)