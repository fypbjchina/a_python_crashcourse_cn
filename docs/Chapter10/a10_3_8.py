# a10_3_8.py
# 调用函数count_words(),for循环处理多个文件
# 第二个文件无法找到，pass静默失败

import a10_3_8_f_count_words as a10_3_8_f

filenames = ['book/alice.txt', 'siddhartha.txt', 'book/moby_dick.txt']
for filename in filenames:
    a10_3_8_f.count_words(filename)