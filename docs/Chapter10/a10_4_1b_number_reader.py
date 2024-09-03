# a10_4_1b_number_reader.py
# 导入模块jsaon
# 读取数据调用load()函数，一个实参：文件对象

import json

filename = 'a10_4_1_numbers.json'
with open(filename) as f:
    num_list = json.load(f)

print(num_list) 