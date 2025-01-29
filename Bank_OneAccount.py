accountName = "Tim"
accountBalance = 100
accountPassword = "apple"

while True:
    
    print("\nPress b to get account balance")
    print("Press d to make deposit")
    print("Press w to make a withdrawal")
    print("Press s to show the account")
    print("Press q to quit\n")

    command = input(f"|Enter Command|\n").lower()
    command = command[0]#Use first letter
    
    if command == "b":
        print("Password Required To Display Balance")
        userPassword = input("Enter accounts password: ").strip()
        if userPassword != accountPassword:
            print("\nInvalid password")
        else:
            print(f"\nAccount Balance: {accountBalance}")
    
    elif command == "d":
        print("Password Required To Make A Deposit")
        userPassword = input("Enter accounts password: ").strip()
        if userPassword != accountPassword:
            print("\nInvalid password")
        else:
            depositAmount = float(input("Enter amount to deposit"))
            if depositAmount < 0:
                print("You cannot deposit a number less than 0")
            else:
                accountBalance += depositAmount
                print(f"Your Total Balance is now {accountBalance}")
    elif command == "w":
        print("Password Required To Make A Deposit")
        userPassword = input("Enter accounts password: ").strip()
        if userPassword != accountPassword:
            print("\nInvalid password")
        else: 
            withdrawAmount = float(input("Enter amount to withdraw"))
            if withdrawAmount > accountBalance:
                print("You cannot withdraw more money than you have")
            elif withdrawAmount < 0:
                print("You cannot withdraw a negative number")
            else:
                accountBalance -= withdrawAmount
                print(f"Successfuly withdrew ${withdrawAmount}\n")
                print(f"Remaining balance {accountBalance}")

    elif command == "s":
        print("Password Required To Make A Deposit")
        userPassword = input("Enter accounts password: ").strip()
        if userPassword != accountPassword:
            print("\nInvalid password")
        else:
            print("Account")
            print(f"Name: {accountName}")
            print(f"Balance: {accountBalance}")
            print(f"Password: {accountPassword}")

    elif command == "q":
        print("Thanks For Using Our Bank!")
        break
    else:
        print("Invalid Command")
