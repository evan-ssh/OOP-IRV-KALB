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

def withdraw(accountNumber, amountToWithdraw, password):
    global accountnamesList, accountBalancesList, accountPasswordsList
    if password != accountPasswordsList[accountNumber]:
        print("Incorrect Password")
        return
    if amountToWithdraw > accountBalancesList[accountNumber]:
        print("You cannot withdraw more than you have")
    accountBalancesList[accountNumber] -= amountToWithdraw
    return accountBalancesList[accountNumber]

def displayMenu():
    print("Press b to get the balance")
    print("press d to make a deposit")
    print("press n to create a new account")
    print("press w to make a withdrawal")
    print("Press s to show all accounts")
    print("Press q to quit")

print("Tims account is account number:", len(accountnamesList))
newAccount("Tim", 100, "soup")
print("Jims account is account number:", len(accountnamesList))
newAccount("Jim",200,"peanut")
while True:
    displayMenu()
    command = input("Enter a command:").lower()
    command = command[0]

    if command == "b":
        print("Get Balance:")
        userAccountNumber = int(input("Enter your account number:"))
        userPassword = input("Enter your password:")
        theBalance = getBalance(userAccountNumber, userPassword)
        print(f"The balance is ${theBalance}")
    
    elif command == "d":
        print("Make a deposit")
        userAccountNumber = int(input("Enter your account number:"))
        userDepositAmount = float(input("Enter the amount to deposit:"))
        userPassword = input("Enter your password:")
        newBalance = deposit(userAccountNumber, userDepositAmount, userPassword)
        print(f"The new balance is ${newBalance}")

    elif command == "n":
        print("Create a new account")
        userName = input("Enter your name:")
        userStartingAmount = float(input("Enter initial deposit:"))
        userPassword = input("Enter a password")
        userAccountNumber = len(accountnamesList)
        newAccount(userName, userStartingAmount, userPassword)
        print(f"Your new accounts number is{userAccountNumber}")

    elif command == "w":
        print("Make a withdrawal")
        userAccountNumber = int(input("Please enter your account number:"))
        userWithdrawalAmount = float(input("Enter the amount to withdraw:"))
        userPassword = input("Enter your password:")
        newBalance = withdraw(userAccountNumber,userWithdrawalAmount,userPassword)
        print(f"The new balance is ${newBalance}")
    elif command == "q":
        print("Thanks for using our bank!")
        break
    else:
        print("Invalid Command.")
