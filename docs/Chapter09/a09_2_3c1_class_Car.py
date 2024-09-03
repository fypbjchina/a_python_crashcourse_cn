# a09_2_3c1_class_Car.py
# 创建一个Car类
# c1. 通过方法increment_odometer()对属性的值进行递增

class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性。"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """返回整洁的描述性信息。"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.upper()
    
    def read_odometer(self):
        """打印一条指出汽车里程的消息。"""
        print(f"This car has already {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值。
        禁止将里程表读数往回调。
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        """将里程表读数增加指定的量。"""
        self.odometer_reading += miles
        
# 创建一个名为odometer_reading 的属性, 并将其初始值设置为0
# 定义read_odometer()方法，获悉汽车的里程
# 定义update_odometer()方法，形参mileage接受一个实参，并赋值给属性odometer_reading
# 添加if-else条件判断，禁止任何人将里程表读数往回调
# 定义increment_odometer()方法, 形参miles接受特定递增的里程值并赋值给属性