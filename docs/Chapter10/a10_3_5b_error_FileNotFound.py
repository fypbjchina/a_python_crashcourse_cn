# a10_3_5_error_FileNotFound.py
# FileNotFoundError是Python找不到要打开的文件时创建的异常
# try-except代码块处理FileNotFoundError异常对象

filename = 'alice.txt' # book/alice.txt

try:
    with open(filename, encoding='utf-8') as f:
        contents =f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")