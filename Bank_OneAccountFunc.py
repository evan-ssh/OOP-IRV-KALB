accountName = ''
accountBalance = 0
accountPassword = ''

def newAccount(name,balance,password):
    global accountName,accountBalance,accountPassword
    accountName = name
    accountBalance = balance
    accountPassword = password

def showAccount():
    global accountName,accountBalance,accountPassword
    print(f"Account name {accountName}")
    print(f"Account balance {accountBalance}")
    print(f"Account password {accountPassword}")