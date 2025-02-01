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


