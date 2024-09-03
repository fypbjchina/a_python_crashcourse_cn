# a09_2_2.py
# 创建一个Car类，给属性指定默认值0

import a09_2_2_class_Car as a09_2_2

my_new_car = a09_2_2.Car('vw', 'passat', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()