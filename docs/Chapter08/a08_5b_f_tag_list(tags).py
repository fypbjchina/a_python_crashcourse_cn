# a08_5b_f_tag_list(tags).py
# 定义函数, 使用for循环遍历打印标签

def tag_list(*tags): # *生成一个空元组
    """打印所有标签 - 标签元素"""
    print(f"List inclues follow tags:")
    for tag in tags:
        print(f"- {tag}")

tag_list('a', 'b', 'c')
tag_list('a', 'b', 'c', 'D', 'E', 'F')