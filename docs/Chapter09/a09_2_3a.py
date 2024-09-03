# a09_2_3a.py
# a. 直接修改属性的值

import a09_2_2_class_Car as a09_2_2

my_new_car = a09_2_2.Car('vw', 'passat', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23 # 修改属性odometer_reading的值为23
my_new_car.read_odometer()