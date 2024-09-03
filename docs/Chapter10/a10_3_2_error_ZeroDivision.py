# a10_3_2_error_ZeroDivision.py
# ZeroDivisionError是个异常对象
# 使用try-except代码块处理异常

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")