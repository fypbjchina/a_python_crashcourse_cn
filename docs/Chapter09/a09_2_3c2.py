# a09_2_3c2.py
# c2. 通过方法对属性的值进行递增，禁止新增里程为负值

import a09_2_3c2_class_Car as a09_2_3c2

my_used_car = a09_2_3c2.Car('vw', 'passat', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500) # 修改属性odometer_reading的值
my_used_car.read_odometer()

my_used_car.increment_odometer(-1000) # 增加里程，追加到属性odometer_reading
my_used_car.read_odometer()