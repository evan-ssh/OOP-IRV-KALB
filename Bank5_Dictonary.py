accountsList = []

def newAccount(name,balance,password):
    global accountsList
    accountDict = {"name":name,"balance":balance,"password":password}
    accountsList.append(accountDict)

def showAccount(accountnumber):
    global accountsList
    AccountDict = accountsList[accountnumber]
    print(f"Account Number:{accountnumber}")
    print(f"Account Nme:{AccountDict['name']}")
    print(f"Acccount Balance: {AccountDict['balance']}")
    print(f"Account Password: {AccountDict['password']}")

