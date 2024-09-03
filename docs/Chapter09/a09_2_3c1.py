# a09_2_3c1.py
# c1. 通过方法对属性的值进行递增

import a09_2_3c1_class_Car as a09_2_3c1

my_used_car = a09_2_3c1.Car('vw', 'passat', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500) # 修改属性odometer_reading的值
my_used_car.read_odometer()

my_used_car.increment_odometer(-1000) # 增加里程100，追加到属性odometer_reading
my_used_car.read_odometer()