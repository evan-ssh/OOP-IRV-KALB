class Account:
    def __init__(self,name,balance,password):
        self.name = name
        self.balance = int(balance)
        self.password = password

def deposit(self,amountToDeposit,password):
    if password != self.password:
        print("Incorrect Password")
        return None
    if amountToDeposit < 0:
        print("You cannot deposit a negative amount")
        return None
    self.balance += amountToDeposit
    return self.balance

def withdraw(self,amountToWithdraw,password):
    if password != self.password:
        print("Incorrect Password")
        return None
    if amountToWithdraw > self.balance:
        print("You cannot withdraw more than what is in your account")
        return None
    if amountToWithdraw < 0:
        print("You cannot withdraw a negative amount")
        return None
    self.balance -= amountToWithdraw
    return self.balance

def getBalance(self,password):
    if password != self.password:
        print("Incorrect Password")
        return None
    else:
        print(f"Your balance is {self.balance}")

def showAccount(self):
    print(f"Account Name:{self.name}")
    print(f"Account Balance:{self.balance}")
    print(f"Account Password:{self.password}")