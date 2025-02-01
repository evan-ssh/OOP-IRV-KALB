accountsList = []

def newAccount(name,balance,password):
    global accountslist
    accountDict = {"name":name,"balance":balance,"password":password}
    accountsList.append(accountDict)