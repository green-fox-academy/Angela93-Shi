# It must have a code, a central bank name and a value field.

class Currency():
    def __init__(self,code,bank_name,value):
        self.code = code
        self.bank_name = bank_name
        self.value =value