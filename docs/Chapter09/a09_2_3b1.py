# a09_2_3b1.py
# b1. 通过定义的方法update_odometer()修改属性的值

import a09_2_3b1_class_Car as a09_2_3b1

my_new_car = a09_2_3b1.Car('vw', 'passat', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23) # 修改属性odometer_reading的值为23
my_new_car.read_odometer()