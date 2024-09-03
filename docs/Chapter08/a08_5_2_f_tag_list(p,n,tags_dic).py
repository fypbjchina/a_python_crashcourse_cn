# a08_5_2_f_tag_list(p,n,tags_dic).py
# 函数形参名 **tags_dic 中的星号让Python创建一个名为 tags_dic 的空字典，并将收到的所有键值对都放到这个字典中。

def tag_list(part, nr, **tags_dic): # *生成一个空字典
    """打印所有标签 - 字典"""
    tags_dic['Part'] = part.title()
    tags_dic['Nr.'] = nr
    return tags_dic


part_tag = tag_list('piston', '01', 
                    Tag='a', Date='20230528',
                   )

print(part_tag)
print(f"{part_tag['Part']}_{part_tag['Nr.']} with tag: {part_tag['Tag']} @ {part_tag['Date']}")