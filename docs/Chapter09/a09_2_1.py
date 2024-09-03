# a09_2_1.py
# 创建一个Car类

import sys
sys.path.insert(0, 'T:/50-ADM/21-BCC/20230308-Python_Beginner/04-Basis/20230615-第9章')

import a09_2_1_class_Car as a09_2_1

my_new_car = a09_2_1.Car('vw', 'passat', 2019)
print(my_new_car.get_descriptive_name())