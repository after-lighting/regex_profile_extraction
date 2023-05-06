import os
import re
import docx2txt

num_formatted_message_item_list = 0
formatted_message_item_list = []
for file_name in os.listdir('data/'):
    # 处理原始的docx文件为元组(group_id, message_id, message_text)--start
    base_dir_path = 'F:/graduation-project/regex/data/'
    docx_handle = docx2txt.process(base_dir_path + file_name)
    message_item_list = re.findall(r'\d+\..*?\n{4}', docx_handle, re.S)
    for message_item in message_item_list:
        try:
            message = re.search(r'(?<=\n{2}).*(?=\n{4})', message_item).group()
        except AttributeError:
            message = ""
        group_message_id = re.search(r'(?<= {4}-).*(?= {6})', message_item).group().split('_')
        item = (group_message_id[0], group_message_id[1], message)
        # item = (group_message_id[0], group_message_id[1], message)
        formatted_message_item_list.append(item)
    # 处理原始的docx文件为元组(group_id, message_id, message_text)--end
    num_formatted_message_item_list += len(formatted_message_item_list)
    
__all__ = ['formatted_message_item_list']