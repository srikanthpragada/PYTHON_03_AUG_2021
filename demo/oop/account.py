class FundsException(Exception):
    def __init__(self, balance, amount):
        self.message = f"Required amount is {amount}, but you only have balance of {balance} in your account!"

    def __str__(self):
        return self.message


class SavingsAccount:
    minbal = 10000

    @staticmethod
    def getminbal():
        return SavingsAccount.minbal

    @classmethod
    def createdefaccount(cls, acno, ahname):
        return cls(acno, ahname, 10000)

    def __init__(self, acno, ahname, balance=0):
        self.acno = acno
        self.customer = ahname
        self.__balance = balance  # Private attribute

    def getbalance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            raise FundsException(self.__balance, amount)


a1 = SavingsAccount(1, "James")
a1.deposit(10000)
a1.withdraw(20000)
print(a1.getbalance())

a2 = SavingsAccount(2, "Andy", 20000)
a3 = SavingsAccount.createdefaccount(10, "Bob")
print(a3.__dict__)
print(a3.acno, a3.ahname, a3._SavingsAccount__balance)
