class Account:
    def __init__(self, name , account, balance):
        self.name = name
        self.account = account
        self.__balance = balance
        
    def addBalance(self , account, balance):
        self.balance += account
        self.__account = account

    def withdraw(self, acount, balance):
        self.account = acount
        self.__balance -= balance

    def get_balance(self):
        return self.__balance 


class SavingAccount(Account):
    def __init__(self, name, account, balance, interest_rate):
        super().__init__(name, account, balance)
        self.interest_rate = interest_rate
    def set_interest(self, inerest):
        return self.get_balance() *  (inerest / 100.00)