accountsList = []

def newAccount(name,balance,password):
    global accountsList
    accountDict = {"name":name,"balance":balance,"password":password}
    accountsList.append(accountDict)
    print(f"Account {name} User Number {len(accountsList)}")

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

def showAllAccounts():
  
    for i, account in enumerate(accountsList):
        print(f"Account {account['name']} : Account Number {i}")

def displayMenu():
    print("'b' to get account Balance")
    print("'d' to make a deposit")
    print("'n' to create a new account")
    print("'w' to make a withdrawal")
    print("'s' to show all accounts")
    print("'q' to exit program")
newAccount("joe",100,"soup")
print(f"accout number {len(accountsList)}")
while True:
    displayMenu()
    command = input("Enter a command:").lower()
    command = command[0]

    if command == "b":
        print("Get Account Balance")
        accountNumber = int(input("Enter Account Number:"))
        password = input("Enter Password:")
        getBalance(accountNumber,password)
    
    elif command == "d":
        print("Make a Deposit")
        accountNumber = int(input("Enter Account Number:"))
        password = input("Enter Password:")
        amount = float(input("Enter Amount to Deposit:"))
        deposit(accountNumber,amount,password)
    elif command == "n":
        print("Creating a new account")
        name = input("Enter Accounts Name:").strip()
        balance = float(input("Enter Starting Balance:"))
        password = input("Enter Password").strip()
        newAccount(name,balance,password)
    elif command == "w":
        print("Making a withdrawal")
        accountNumber = int(input("Enter Account Number:"))
        password = input("Enter Password:")
        amount = float(input("enter amount to withdraw:"))
        withdraw(accountNumber,amount,password)
    elif command == "s":
        print("Showing all accounts")
        showAllAccounts()
    