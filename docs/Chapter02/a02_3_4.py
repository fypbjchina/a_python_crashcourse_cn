# a02_3_4.py
# 方法strip(), rstrip(), lstrip()删除空白

text = '  --Beginner--  '

print(f"{text}{text}{text}")

print(f"{text.strip()}{text.strip()}{text}")
print(f"{text.rstrip()}{text.rstrip()}{text}")
print(f"{text.lstrip()}{text.lstrip()}{text}")