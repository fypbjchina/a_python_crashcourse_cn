# a09_4.py
# 各种导入类的方法：from-import-as

# 9.4.1　导入单个类
from a09_4_class_Car_Battery_E_Car import Car

my_car = Car('vw', 'passat', 2019)
print(my_car.get_descriptive_name())

# 9.4.3　在一个模块中存储多个类
from a09_4_class_Car_Battery_E_Car import Car, ECar

my_ö_car = Car('vw', 'passat', 2019)
my_e_car = ECar('byd', 'tang', 2025)

my_ö_car.fill_tank()
my_e_car.fill_tank()

# 9.4.4　导入整个模块
import a09_4_class_Car_Battery_E_Car as class_car

my_ö_car = class_car.Car('vw', 'passat', 2019)
my_e_car = class_car.ECar('byd', 'tang', 2025)

print(my_ö_car.get_descriptive_name())
print(my_e_car.get_descriptive_name())