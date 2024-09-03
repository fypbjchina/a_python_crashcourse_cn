# a10_1_2a_file_reader.py
# 相对文件路径是相对于当前运行的程序所在目录
# 显示文件路径Windows系统使用反斜杠(\),Python中可以使用斜杠(/, \\, r'\')

with open('pi/pi_digits.txt') as file_object:
    contents = file_object.read()
    
print(contents.rstrip())