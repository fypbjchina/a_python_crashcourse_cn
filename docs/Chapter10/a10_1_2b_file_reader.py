# a10_1_2b_file_reader.py
# 绝对文件路径是文件在计算机中的准确位置

with open('T:/50-ADM/21-BCC/20230308-Python_Beginner/00-Reference/00-Book/a-Python编程：从入门到实践/02-源代码文件/chapter_10/pi_digits.txt') as file_object:
    contents = file_object.read()
    
print(contents.rstrip())