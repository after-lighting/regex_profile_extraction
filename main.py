from convert_docx_format import convert_docx_format
from reg_rule_class import messageReg

import os
import configparser

all_formatted_message_item_list = []
for file_name in os.listdir('data/'):
    base_dir_path = 'F:/graduation-project/regex/data/'
    formatted_message_item_list = convert_docx_format(base_dir_path + file_name)
    all_formatted_message_item_list.extend(formatted_message_item_list)

# ------- have done all message formatted -------
def reg_search(all_formatted_message_item_list):
    res_list = []
    config_handle = configparser.ConfigParser(interpolation=None)
    # 必须要禁止变量替换因为会读入$
    config_handle.read('regex_config.ini')
    for section in config_handle.sections():
        for reg_key, reg_value in config_handle.items(section):
            messageRegInstance = messageReg('{} : {}'.format(section, reg_key))
            messageRegInstance.reg_expression = reg_value
    for messageRegInstance in messageReg.get_instances():
        for message_item in all_formatted_message_item_list:
            messageRegInstance.reg_search(message_item)
        res_item = {
            messageRegInstance.regexName : messageRegInstance.reg_output_list
        }
        res_list.append(res_item)
    return res_list

reg_search(all_formatted_message_item_list)