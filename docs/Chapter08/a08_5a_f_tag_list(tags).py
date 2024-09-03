# a08_5a_f_tag_list(tags).py
# 定义函数: 形参名 *tags 中的星号让Python创建一个名为 tags 的空元组，并将收到的所有值都封装到这个元组中。

def tag_list(*tags): # *生成一个空元组
    """打印所有标签 - 元组"""
    print(tags)

tag_list('a', 'b', 'c')
tag_list('a', 'b', 'c', 'D', 'E', 'F')