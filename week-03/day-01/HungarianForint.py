# It must accept a value.
# The code must be "HUF" by default.
# The central bank name must be "Hungarian National Bank" by default.

from currency import Currency

class HungarianForint():
    def __init__(self,value,code='HUF',bank_name='Hungarian National Bank'):
        Currency.__init__(self,value,code,bank_name)
        self.code = code
        self.bank_name = bank_name
        self.value=value

hungarianForint = HungarianForint(100)