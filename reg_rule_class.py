# 1. url link
# 2. account (twitter, facebook, linkedin, youtube, qq, weixin, weibo)
# 3. phone number
# 4. email
# 5. IP address
# 6. Bitcoin address
import re
class regBase():
# 仅处理字符串
    def __init__(self, regname) -> None:
        self.regexName = regname

    @property
    def reg_expression(self):
        return self.reg_exp
    
    @reg_expression.setter
    def reg_expression(self, regex):
        self.reg_exp = regex
        # 这里是一个很容易忽略又必须注意的细节：setter的函数名字不能与类中实际的属性名相同
        # 因为我们在外部访问这个属性的时候并不是单纯读个值，而是运行这函数，因此若是两者名字相同，那么将陷入死循环

    def reg_search(self, target_text):
        if not isinstance(target_text, str):
            raise TypeError("验证正则表达的目标语句必须为字符串类型")
        reg_pattern = re.compile(fr'{self.reg_expression}')
        # fr 代表 formatted r
        search_res = reg_pattern.search(target_text)
        return search_res
        
class messageReg(regBase):
# 处理包含待处理字符串的一整条消息（含群组、消息id等）
# 共享同一类规则的结果
    __instances__ = []

    def __init__(self, regname) -> None:
        super().__init__(regname)
        self.reg_output_list = []
        self.__class__.__instances__.append(self)

    def get_reg_output_list(self):
        return self.reg_output_list
    
    @classmethod
    def get_instances(cls):
        return cls.__instances__

    def reg_search(self, message_item):
        search_res = super().reg_search(message_item[2])
        if search_res is not None:
            self.reg_output_list.append(message_item)