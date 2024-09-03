# a10_1_5_file_reader.py
# 方法readlines()读取文件每一行，存储到列表lines
# for循环遍历列表lines的每一行line
# rstrip()删除每行末尾的换行符
# strip()删除每行左边的空格

filename = 'a10_1_1a_pi_digits.txt' # or 'pi/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip() # or strip()删除每行左边的空格

print(pi_string)
print(len(pi_string))