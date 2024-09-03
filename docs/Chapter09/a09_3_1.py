# a09_3_1.py
# super().__init__(make, model, year)调用父类的方法__init__()
# 确认ECar类具备普通Car类的行为

import a09_3_1_class_Car_E_Car as a09_3_1

my_e_car = a09_3_1.ECar('byd', 'tang', 2025)
print(my_e_car.get_descriptive_name())