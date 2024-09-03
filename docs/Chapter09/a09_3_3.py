# a09_3_3.py
# ECar类同名重写Car类方法fill_tank()

import a09_3_3_class_Car_E_Car as a09_3_3

my_ö_car = a09_3_3.Car('vw', 'passat', 2019)
my_e_car = a09_3_3.ECar('byd', 'tang', 2025)

print(my_e_car.get_descriptive_name())

my_e_car.describe_battery()

my_ö_car.fill_tank()
my_e_car.fill_tank()