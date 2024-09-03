# a09_3_2_class_Car_E_Car.py
# 创建一个Car类,ECar类
# 使用继承,ECar类获得Car类方法fill_tank()，同名重写父类方法

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
        return long_name.lower()
    
    def read_odometer(self):
        """打印一条指出汽车里程的消息。"""
        print(f"This car has {self.odometer_reading} miles on it.")
        
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
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")
            
    def fill_tank(self):
        """打印一条油箱容量的消息。"""
        print("Please attention the Öl type!")

class ECar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性。
        再初始化电动汽车特有的属性。
        """
        super().__init__(make, model, year)
        self.battery_size = 75
        
    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print(f"This car has a {self.battery_size}-kWh battery.")
        
    def fill_tank(self):
        """电动汽车没有油箱。"""
        print("This is a E_Car, doesn't have an oil tank!")
    
# 创建一个名为odometer_reading的属性, 并将其初始值设置为0

# 定义read_odometer()方法，获悉汽车的里程

# 定义update_odometer()方法，形参mileage接受一个实参，并赋值给属性odometer_reading
# 添加if-else条件判断，禁止任何人将里程表读数往回调

# 定义increment_odometer()方法, 形参miles接受特定递增的里程值并赋值给属性
# 添加if-else条件判断，禁止新增里程为负值

# 定义子类ECar时，必须在圆括号内指定父类的名称--> ECar(Car)
# 父类也称为超类(superclass)，函数super()调用父类的方法

# ECar类添加特有属性self.battery_size,指定默认值
# ECar类定义特有方法describe_battery()

# Car类定义了方法fill_tank()
# ECar类同名重写父类方法fill_tank()