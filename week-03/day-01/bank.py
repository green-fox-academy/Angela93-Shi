# It must have a BankAccount list.
# It must have a createAccount method with a BankAccount as an input parameter 
# it must add the BankAccount to the list
# It should have a getAllMoney method, which returns the sum of 
# the accounts' money (sum of Currency values regardless of the Currency type).
from bank_account import BankAccount

class Bank():
    def __init__(self):
        self.bankaccount_list = []
    
    def createAccount(self,bank_account):
        self.bankaccount_list.append(bank_account)
        return self.bankaccount_list

       
    def getAllMoney(self):
        sum_of_money = 0
        for accounts in self.bankaccount_list:
            sum_of_money += accounts.currency
        return sum_of_money
        

bank = Bank()
bank_account = BankAccount('Angela','3287453512355',10000)
bank_list = bank.createAccount(bank_account)
print(bank.getAllMoney())