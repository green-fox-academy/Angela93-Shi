# It must accept a value.
# The code must be "USD" by default.
# The central bank name must be "Federal Reserve System" by default.
from currency import Currency

class USDDollar():
    def __init__(self,value,code='USD',bank_name='Federal Reserve System'):
        Currency.__init__(self,value,code,bank_name)
        self.code = code
        self.bank_name = bank_name
        self.value = value

usd_dollar = USDDollar(200)
