# a10_3_7_f_count_words.py
# 函数count_words()用于计算文件包含的单词数量
# try-except-else 代码块, pass静默失败

def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents =f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")