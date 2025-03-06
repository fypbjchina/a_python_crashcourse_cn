"""
# 示范案例封神人物系列
# 定义诸多角色的函数：哪吒，太乙真人，申公豹，。。。


需求定义：
角色哪吒的生命值测试
- 角色初始生命值100，最大不超过150，最低不低于0
- get_damage()遭遇伤害,get_heal()接受治疗
- 生命值=0：=Game Over
"""

class NaZha3Taizi:
    def __init__(self):
        self.health=100
        self.is_alive=True

    def get_damage(self,damage:int):
        self.health=max(0,self.health-damage)
        if self.health==0:
            self.is_alive = False

    def get_heal(self, points:int):
        self.health=min(150,self.health+points)
        if self.health>0:  # 治疗后复活检测
            self.is_alive=True