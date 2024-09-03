# a10_3_3_error_ZeroDivision.py
# 执行除数为0的除法运算时,程序没有采取任何处理错误的措施,它将崩溃

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)