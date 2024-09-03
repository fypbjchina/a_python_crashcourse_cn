# a10_2_1_file_writer.py
# 调用open() 时提供了两个实参: 文件名，读/写模式
# 指定读取模式 ('r'),写入模式('w'), 附加模式('a')或读写模式('r+')
# 'w' 模式会覆盖原有文件内容
# Python只能将字符串写入文本文件, 数值数据必须先使用函数str()将其转换为字符串格式

filename = 'a10_2_1_python_beginner.txt'

with open(filename, 'w') as file_object:
    file_object.write("Hello, Python Beginner!")