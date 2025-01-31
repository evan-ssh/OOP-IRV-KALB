account0Name = ""
account0Balance = 0
account0Pass = ""
account1Name = ""
account1Balance = 0
account1Pass = ""
nAccounts = 0
def newAccount(accountNumber,name,balance,password):
    global account0Name,account0Balance,account0Pass
    global account1Name,account1Balance,account1Pass
    
    if accountNumber == 0:
        account0Name = name
        account0Balance = balance
        account0Pass = password
    if accountNumber == 1:
        account1Name = name
        account1Balance = balance
        account1Pass = password

def showAccount():
    global account0Name, account0Balance, account0Pass
    if account0Name != "":
        print(f"Account name {account0Name}")
        print(f"Account balance {account0Balance}")
        print(f"Account password {account0Pass}")
    if account1Name != "":
        print(f"Account name {account1Name}")
        print(f"Account balance {account1Balance}")
        print(f"Account password {account1Pass}")

def getBalance(accountNumber,password):
    global account0Name, account0Balance, account0Pass
    global account1Name, account1Balance, account1Pass
    if accountNumber == 0:
        if password != account0Pass:
            print("Invalid Password")
            return
        return account0Balance
    if accountNumber == 1:
        if password != account1Pass:
            print("Invalid Password")
            return
        return account1Balance
    
def deposit(accountNumber,password):
    global account0Name, account0Balance, account0Pass
    global account1Name, account1Balance, account1Pass
    if password != account0Pass or account1Pass:
        print("Incorrect Password")
        return
    
    if accountNumber == 0:
        depositAmount = float(input("Enter deposit amount: "))
        if depositAmount < 0:
            print("You can not deposit a negative amount")
            return 
        else:
            account0Balance += depositAmount
            return account0Balance

    if accountNumber == 1:
        depositAmount = float(input("Enter deposit amount: "))
        if depositAmount < 0:
            print("You can not deposit a negative amount")
            return
        else:
            account1Balance += depositAmount
            return account1Balance
        