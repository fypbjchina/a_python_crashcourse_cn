# a08_5_1_f_tag_list(n,tags).py
# 定义函数, 接纳两种实参 - 位置实参 01/02 + 任意实参 *tags

def tag_list(nr, *tags): # *生成一个空元组
    """打印所有标签- 标签元素"""
    print(f"Sample_{nr} inclues follow tags:")
    for tag in tags:
        print(f"- {nr}_{tag}")

tag_list('01', 'a', 'b', 'c')
tag_list('02', 'a', 'b', 'c', 'D', 'E', 'F')