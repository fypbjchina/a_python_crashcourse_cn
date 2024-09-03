# a10_1_7_file_reader.py
# 检查生日mmddyy是否包含在圆周率值的前1 000 000位中

filename = 'a10_1_6_pi_million_digits.txt' # or 'pi/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy:\t")

if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")