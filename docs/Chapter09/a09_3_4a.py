# a09_3_4a.py
# 使用的是Battery类的一个实例作为ECar类的一个属性

import a09_3_4a_class_Car_Battery_E_Car as a09_3_4a

my_e_car = a09_3_4a.ECar('byd', 'tang', 2025)
print(my_e_car.get_descriptive_name())

# ECar属性battery通过实例调用Battery方法
my_e_car.battery.describe_battery()