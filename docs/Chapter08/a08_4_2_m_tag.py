# a08_4_2_m_tag.py
# 模块tag包含两个函数，第一个函数负责打印标签，第二个负责显示打印过后的标签信息
# 禁止函数修改列表: 传递给函数列表副本 - 切片表示法[:]

def print_tags(new_tags, used_tags):
    """模拟打印每个标签，直到没有标签为止。
    使用过的标签，都将移动到列表used_tags中。
    """
    while new_tags:
        use_tag = new_tags.pop() # pop()默认弹出列表最后一个元素，pop(0)弹出第一元素
        print(f"Current use tag:\t{use_tag}")
        used_tags.append(use_tag.lower())
            
def show_tags(new_tags, used_tags):
    """显示打印过后的标签列表状态"""
    used_tags = sorted(used_tags)
    print("\nThe tags status are:")
    print(f"Used tags list:\t{used_tags}")
    print(f"New tags list:\t{new_tags}")

new_tags = ['a','b','c','D','E','F']
used_tags = []

print_tags(new_tags[:], used_tags) # 向函数传递列表的副本, 函数所做的任何修改都只影响副本，而原件丝毫不受影响。
show_tags(new_tags, used_tags)