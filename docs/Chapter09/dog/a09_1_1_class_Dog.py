# a09_1_1_class_Dog.py
# 创建一个Dog类

class Dog:
    """一次模拟小狗的简单尝试"""
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到命令时蹲下。"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """模拟小狗收到命令时打滚。"""
        print(f"{self.name} rolled over!")
    

# 类中的函数称为方法, __init__() 是一个特殊方法，
# 根据类创建新实例时，Python都会自动运行它
# 方法__init__() 定义成包含三个形参：self,name和age，形参self必不可少
# 每个实例自动传入实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法
# self 为前缀的变量可供类中的所有方法使用,可以通过类的任何实例来访问
# 实例访问的变量称为属性, 如self.name, self.age
# Dog 类还定义了另外两个方法：sit() 和roll_over()