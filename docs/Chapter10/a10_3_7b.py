# a10_3_7b.py
# 调用函数count_words(),for循环处理多个文件

import a10_3_7_f_count_words as a10_3_7_f

filenames = ['book/alice.txt', 'siddhartha.txt', 'book/moby_dick.txt']
for filename in filenames:
    a10_3_7_f.count_words(filename)