# a10_1_4_file_reader.py
# 方法readlines()读取文件每一行，存储到列表lines
# for循环遍历列表lines的每一行line

filename = 'a10_1_1a_pi_digits.txt' # or 'pi/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.rstrip())