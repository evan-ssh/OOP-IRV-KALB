accountName = ''
accountBalance = 0
accountPassword = ''

def newAccount(name,balance,password):
    global accountName,accountBalance,accountPassword
    accountName = name
    accountBalance = balance
    accountPassword = password

def showAccount(password):
    global accountName,accountBalance,accountPassword
    if password != accountPassword:
        print("Invalid Password")
        return
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
    return accountBalance

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
    return accountBalance
def displayMenu():
    print("Press b to get the balance")
    print("Press d to make deposit")
    print("Press w to make withdrawal")
    print("Press s to show account details")
    print("Press q to quit")
    
newAccount("Josh",233,"soup")
while True:
    displayMenu()
    command = input("Enter a command:").strip().lower()
    command = command[0]

    if command == "b":
        print("Get balance")
        password = input("Enter your password:")
        balance = getBalance(password)
        print(f"Your balance is ${balance}")
    elif command == "d":
        print("Make a Deposit")
        password = input("Enter your password:")
        amount = (float(input("Enter the amount to deposit:")))
        newBalance = deposit(amount,password)
        print(f"Your new balance is ${newBalance}")
    elif command == "w":
        print("Make a Withdrawal")
        password = input("Enter your password:")
        amount = (float(input("Enter the amount to Withdraw:")))
        newBalance = withdraw(amount,password)
        print(f"Your new balance is ${newBalance}")
    elif command == "s":
        print("Show Account Details")
        password = input("Enter your password:")
        newBalance = showAccount(password)
    elif command == "q":
        print("Thanks for using our bank")
        break
    else:
        print("Invalid command")