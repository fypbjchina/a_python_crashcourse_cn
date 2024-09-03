# a02_3_2.py
# f(), r(), title(), upper()...

first_name = "beginner"
last_name = "python"
full_name = f"{first_name.title()} {last_name.upper()}"

print (full_name)

full_name = f"{first_name}@{last_name}"
message_f = f"Welcome, {full_name.title()}!"
message_r = r"Welcome, {full_name.title()}!"
message_b = b"Welcome, {full_name.title()}!"

print(full_name.title())
print(message_f)
print(message_r)
print(message_b)