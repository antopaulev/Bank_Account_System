from models.account import Account

accounts = []

while True:
    print("\n====Bank Account System====")
    print("\n1.Create Account")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.Check Balance")
    print("5.Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        name = input("\nEnter your name: ")
        balance = int(input("Enter initial balance: "))
        
        if balance >= 500:
            acc= Account(name, balance)
            accounts.append(acc)
            print("\nAccount created successfully")
        else:
            print("\nMinimum initial deposit is 500 ") 
       
    elif choice == 2:
        if not accounts:
            print("Create an account first")
        else:
            amount = int(input("\nEnter deposit amount: "))
            accounts[-1].deposit(amount)

    elif choice == 3:
        if not accounts:
            print("Create an account first")
        else:
            amount = int(input("\nEnter the withdrawal amount: "))
            accounts[-1].withdraw(amount)

    elif choice == 4:
        if not accounts:
            print("Create an account first")
        else:
            print(f"\nBalance: {accounts[-1].check_balance()}")    

    elif choice == 5:
        print("Program Exited")
        break

    else :
        print("Invalid Option. Please Try Again.")