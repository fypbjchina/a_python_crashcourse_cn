# a09_2_2_class_Car.py
# 创建一个Car类，给属性指定默认值

class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性。"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 10000
    
    def get_descriptive_name(self):
        """返回整洁的描述性信息。"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.upper()
    
    def read_odometer(self):
        """打印一条指出汽车里程的消息。"""
        print(f"This car has {self.odometer_reading} miles on it.")
        
# 创建一个名为odometer_reading 的属性, 并将其初始值设置为0
# 定义read_odometer()方法，获悉汽车的里程