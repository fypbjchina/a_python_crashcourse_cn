# a08_6_4.py
# 模块a08_4_1_m_tag.py
# 使用as给模块指定别名

import a08_4_1_m_tag as tag

new_tags = ['a','b','c','D','E','F']
used_tags = []

tag.print_tags(new_tags, used_tags)
tag.show_tags(new_tags, used_tags)