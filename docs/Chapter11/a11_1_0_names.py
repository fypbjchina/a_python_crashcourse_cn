# a11_1_0_names.py
# 输入名和姓，确保调用的函数get_formatted_name()可以正常工作

from a11_1_0_f_name_function_fl import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")