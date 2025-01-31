accountnamesList = []
accountBalancesList = []
accountPasswordsList = []

def newAccount(name,balance,password):
    global accountnamesList,accountBalancesList,accountPasswordsList
    accountnamesList.append(name)
    accountBalancesList.append(balance)
    accountPasswordsList.append(password)

def showAccount(accountNumber):
    global accountnamesList, accountBalancesList, accountPasswordsList
    print(f"Account number {accountNumber}")
    print(f"Account name {accountnamesList[accountNumber]}")
    print(f"Account balance {accountBalancesList[accountNumber]}")
    print(f"Account password {accountPasswordsList[accountNumber]}")