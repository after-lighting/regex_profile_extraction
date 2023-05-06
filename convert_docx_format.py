import re
import docx2txt

def convert_docx_format(docx_path):
    formatted_message_item_list = []
    docx_handle = docx2txt.process(docx_path)
    message_item_list = re.findall(r'\d+\..*?\n{4}', docx_handle, re.S)
    for message_item in message_item_list:
        try:
            message = re.search(r'(?<=\n{2}).*(?=\n{4})', message_item).group()
        except AttributeError:
            message = ""
        group_message_id = re.search(r'(?<= {4}-).*(?= {6})', message_item).group().split('_')
        item = (group_message_id[0], group_message_id[1], message)
        # 原始的docx文件处理为元组
        formatted_message_item_list.append(item)
    return formatted_message_item_list
