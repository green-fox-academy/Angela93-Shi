# It must have a name a pin code and a Currency.
# It must have a deposit method that takes a value parameter 
# check if the given parameter is positive
# then adds the parameter to the Currency's value field
# It must have a withdraw method with two parameters: a pin code and an amount 
# It must check if the given pin is correct (equals with the original pin)
# and the Currency's value is more than the amount parameter
# If so, subtract the amount from the Currency's value and return with the amount.
# Otherwise don't modify the Currency's value and return with 0.

class BankAccount():
    def __init__(self,name,pin_code,currency):
        self.name = name
        self.pin_code = pin_code
        self.currency = currency
    
    def deposit(self,value):
        try:
            if value > 0:
                self.currency += value
        except:
            pass
    
    def withdraw(self,pin_code,amount):
        try:
            if self.pin_code == pin_code and amount < self.currency:
                self.currency = self.currency - amount
                return amount
        except:
            return 0

