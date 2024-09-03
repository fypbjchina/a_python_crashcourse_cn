# a09_1_1b.py
# b. 使用绝对路径导入dog.py模块

import sys
sys.path.insert(0, 'T:/50-ADM/21-BCC/20230308-Python_Beginner/04-Basis/20230615-第9章')

from a09_1_1_class_Dog import Dog #从模块a09_1_1_class_Dog.py中导入类Dog

my_dog = Dog('dahei', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")