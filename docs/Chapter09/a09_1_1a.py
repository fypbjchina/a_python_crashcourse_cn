# a09_1_1a.py
# a. 使用绝对路径导入dog.py模块

import sys
sys.path.insert(0, 'B:/04_Beginner/01_GitHub/fypbjchina2023/a_PythonCrashCourse/Chapter09')

import a09_1_1_class_Dog as a09_1_1 # 导入模块a09_1_1_class_Dog.py

my_dog = a09_1_1.Dog('dahei', 3) # 从模块dog.py中调用类Dog

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")