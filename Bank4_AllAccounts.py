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

def getBalance(accountNumber,password):
    global accountnamesList, accountBalancesList, accountPasswordsList
    if password != accountPasswordsList[accountNumber]:
        print("Invalid Password")
        return
    return accountBalancesList[accountNumber]

def deposit(accountNumber, amountToDeposit, password):
    global accountnamesList, accountBalancesList, accountPasswordsList
    if password != accountPasswordsList[accountNumber]:
        print("Incorrect Password") 
    if amountToDeposit < 0:
        print("Invalid Amount")
        return
    accountBalancesList[accountNumber] += amountToDeposit
    return accountBalancesList[accountNumber]