# a10_2_3_file_writer.py
# 写入模式'w'会覆盖原有文件内容，附加模式'a'只添加不覆盖文件内容

filename = 'a10_2_1_python_beginner.txt'

with open(filename, 'a') as file_object:
    file_object.write("\n\n------Adding Information------")
    file_object.write("\nI love using Python to learn Math.")