# a10_4_1a_number_writer.py
# 导入模块jsaon
# 存储数据调用dump()函数，两个实参：数据，文件对象

import json

numbers = [10, 20, 30, 40, 50]
print(f"Numbers list:\t{numbers}")

filename = 'a10_4_1_numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
    
with open(filename) as f:
    contents = f.read()
    print(f"Numbers.json:\t{contents}")