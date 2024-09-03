# a10_1_6_file_reader.py
# 处理小数点后1 000 000位的圆周率值

filename = 'a10_1_6_pi_million_digits.txt' # or 'pi/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))