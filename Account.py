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