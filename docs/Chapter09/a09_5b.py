# a09_5b.py
# 模块random包含函数choice(),它将一个列表或元组作为参数,并随机返回其中的一个元素

from random import choice

readers = ['zhang 3', 'li 4', 'wang 5', 'xiao 2']

luck_name = choice(readers)

print(f"{luck_name.title()} is the next leading reader!")