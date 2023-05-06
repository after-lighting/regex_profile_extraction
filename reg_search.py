from reg_rule_class import messageReg
from convert_docx_format import formatted_message_item_list

import configparser

config_handle = configparser.ConfigParser(interpolation=None)
# 必须要禁止变量替换因为会读入$
config_handle.read('regex_config.ini')
for section in config_handle.sections():
    for reg_key, reg_value in config_handle.items(section):
        messageRegInstance = messageReg('{} : {}'.format(section, reg_key))
        messageRegInstance.reg_expression = reg_value
for messageRegInstance in messageReg.get_instances():
    for message_item in formatted_message_item_list:
        messageRegInstance.reg_search(message_item)
    print(messageRegInstance.reg_output_list)
    