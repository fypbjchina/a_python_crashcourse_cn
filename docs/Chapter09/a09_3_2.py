# a09_3_2.py
# ECar类定义特有属性battery_size
# ECar类定义特有方法describe_battery()

import a09_3_2_class_Car_E_Car as a09_3_2

my_e_car = a09_3_2.ECar('byd', 'tang', 2025)
print(my_e_car.get_descriptive_name())

my_e_car.describe_battery()