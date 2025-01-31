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

def getBalance(password):
    global accountName,accountBalance,accountPassword
    if password !=  accountPassword:
        print("Invalid Password")
        return
    return accountBalance

def deposit(amount,password):
    global accountName, accountBalance, accountPassword
    if amount < 0:
        print("You can not deposit a negative amount")
        return 
    if password != accountPassword:
        print("Incorrect Password")
        return
    accountBalance += amount
    print(f"Amount Deposited {amount}")

def withdraw(amount,password):
    global accountName, accountBalance, accountPassword
    if amount < 0:
        print("You can not withdraw a negative amount")
        return
    if password != accountPassword:
        print("Incorrect Password")
        return
    accountBalance -= amount
    print(f"Amount Withdrawn {amount}")
    