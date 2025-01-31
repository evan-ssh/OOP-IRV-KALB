accountnamesList = []
accountBalancesList = []
accountPasswordsList = []

def newAccount(name,balance,password):
    global accountnamesList,accountBalancesList,accountPasswordsList
    accountnamesList.append(name)
    accountBalancesList.append(balance)
    accountPasswordsList.append(password)
    