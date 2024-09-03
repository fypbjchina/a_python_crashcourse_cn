# a09_2_3b2.py
# b2. 通过定义的方法update_odometer()修改属性的值，禁止里程回调

import a09_2_3b2_class_Car as a09_2_3b2

my_new_car = a09_2_3b2.Car('vw', 'passat', 2019)
print(my_new_car.get_descriptive_name())

print(my_new_car.update_odometer(100)) # 修改属性odometer_reading的值
my_new_car.read_odometer()