accountsList = []

def newAccount(name,balance,password):
    global accountsList
    accountDict = {"name":name,"balance":balance,"password":password}
    accountsList.append(accountDict)

def showAccount(accountnumber):
    global accountsList
    AccountDict = accountsList[accountnumber]
    print(f"Account Number:{accountnumber}")
    print(f"Account Name:{AccountDict['name']}")
    print(f"Acccount Balance: {AccountDict['balance']}")
    print(f"Account Password: {AccountDict['password']}")

def getBalance(accountnumber,password):
    global accountsList
    accountDict = accountsList[accountnumber]
    if password != accountDict['password']:
        print("Invalid Password")
        return
    else:
        print(f"Account Balance:{accountDict['balance']}")

def deposit(accountnumber, amountToDeposit, password):
    global accountsList
    accountDict = accountsList[accountnumber]
    if password != accountDict['password']:
        print("Incorrect Password")
        return
    if amountToDeposit < 0:
        print("You cannot deposit a negative amount")
        return
    accountDict['balance'] += amountToDeposit
    print(f"{amountToDeposit} has been depositd to your account, New Total {accountDict['balance']}")
    return accountDict['balance']

def withdraw(accountnumber, amountToWithdraw, password):
    global accountsList
    accountDict = accountsList[accountnumber]
    if password != accountDict['password']:
        print("Incorrect Password")
        return
    if amountToWithdraw < 0:
        print("You cannot deposit a negative amount")
        return
    accountDict['balance'] += amountToWithdraw
    print(f"{amountToWithdraw} has been depositd to your account, New Total {accountDict['balance']}")
    return accountDict['balance']

def displayMenu():
    print("'b' to get account Balance")
    print("'d' to make a deposit")
    print("'n' to create a new account")
    print("'w' to make a withdrawal")
    print("'s' to show all accounts")
    print("'q' to exit program")
