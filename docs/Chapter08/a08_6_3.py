# a08_6_3.py
# 模块a08_4_1_m_tag.py
# 使用as给函数指定别名


from a08_4_1_m_tag import print_tags as pts
from a08_4_1_m_tag import show_tags as sts

new_tags = ['a','b','c','D','E','F']
used_tags = []

pts(new_tags, used_tags)
sts(new_tags, used_tags)# a08_6_3.py