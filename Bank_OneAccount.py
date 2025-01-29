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