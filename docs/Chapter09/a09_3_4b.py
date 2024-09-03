# a09_3_4b.py
# Battery类新增方法get_range()

import a09_3_4b_class_Car_Battery_E_Car as a09_3_4b

# 创建一个ECar实例my_e_car
my_e_car = a09_3_4b.ECar('byd', 'tang', 2025)
print(my_e_car.get_descriptive_name())

# 创建一个Battery实例battery100
battery100 = a09_3_4b.Battery(100)
battery100.describe_battery()
battery100.get_range()

# ECar属性battery通过实例调用Battery方法
my_e_car.battery.describe_battery()
my_e_car.battery.get_range()