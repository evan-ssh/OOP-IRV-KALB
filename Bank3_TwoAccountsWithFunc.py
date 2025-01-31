account0Name = ""
account0Balance = 0
account0Pass = ""
account1Name = ""
account1Balance = 0
account1Pass = ""
nAccounts = 0
def newAccount(accountNumber,name,balance,password):
    global account0Name,account0Balance,account0Pass
    global account1Name,account1Balance,account1Pass
    
    if accountNumber == 0:
        account0Name = name
        account0Balance = balance
        account0Pass = password
    if accountNumber == 1:
        account0Name = name
        account0Balance = balance
        account0Pass = password
