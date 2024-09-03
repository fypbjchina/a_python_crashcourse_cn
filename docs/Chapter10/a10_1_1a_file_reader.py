# a10_1_1a_file_reader.py
# 关键字with在不再需要访问文件后将其关闭 
# 函数open()接受一个参数：要打开的文件的名称, 返回一个表示文件的对象，赋值给变量file_object
# 方法read()读取这个文件的全部内容，并将其作为一个字符串赋给变量contents
# 方法rstrip()删除多出来的空行

with open('a10_1_1a_pi_digits.txt') as file_object:
    contents = file_object.read()
    
print(contents.rstrip())