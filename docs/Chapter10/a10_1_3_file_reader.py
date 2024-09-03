# a10_1_3_file_reader.py
# 赋值变量filename，表示文件位置的字符串
# for循环遍历文件对象file_object的每一行

filename = 'pi/pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)
        # print(line.rstrip()) # 方法rstrip()删除多出来的空行