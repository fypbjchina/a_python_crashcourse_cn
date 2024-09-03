# a08_4_1b_m_tag.py
# 模块tag包含两个函数，第一个函数负责打印标签，第二个负责显示打印过后的标签信息
# 使用del语句删除

def print_tags(new_tags, used_tags):
    """模拟打印每个标签，直到没有标签为止。
    使用过的标签，都将移动到列表used_tags中。
    """
    while new_tags:
        for x in new_tags:
            print(f"Current use tag:\t{new_tags[0]}")
            used_tags.append(new_tags[0].lower())
            del new_tags[0] # del语句删除列表中第一位置的元素 ?
            print(new_tags)
            
def show_tags(new_tags, used_tags):
    """显示打印过后的标签列表状态"""
    used_tags = sorted(used_tags)
    print("\nThe tags status are:")
    print(f"Used tags list:\t{used_tags}")
    print(f"new tags list:\t{new_tags}")

new_tags = ['a','b','c','D','E','F']
used_tags = []

print_tags(new_tags, used_tags)
show_tags(new_tags, used_tags)