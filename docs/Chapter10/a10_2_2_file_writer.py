# a10_2_2_file_writer.py
# 函数write() 不会在写入的文本末尾添加换行符
# 空格、制表符\t和空行\n来设置这些输出的格式

filename = 'a10_2_1_python_beginner.txt'

with open(filename, 'w') as file_object:
    file_object.write("------Python Beginner------")
    file_object.write("\nHello, Python Beginner!")
    file_object.write("\nWelcome to the Python world!")