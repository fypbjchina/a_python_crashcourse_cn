# a10_3_6b_error_FileNotFound.py
# 方法split()以空格为分隔符将字符串分拆成多个部分,并将这些部分存储到列表中
# try-except-else 代码块

filename = 'book/alice.txt' # book/alice.txt

try:
    with open(filename, encoding='utf-8') as f:
        contents =f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # 计算该文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")