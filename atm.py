def main():
    print("Welcome to the ATM!")
    while True:
        print("\nPlease choose an option:")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")        
        
        x = input("Enter your choice (1-3):")
    
        if x == '1':
                create_account()
        elif x == '2':  
                login()
        elif x == '3':
                print("Thank you for using the ATM. Goodbye!")
        break
    
    main()

    def create_account():
        new_data = {new_username, new_password, new_value}
        new_username = input("Enter your desired username:")
        new_password = input("Enter your desired password:")
        new_value = input("Enter your initial deposit amount:")
        print("Account created successfully!")

    def login():
        data = {["user1", "pass1", 1000], ["user2", "pass2", 1500]}  # Example user data
        username = input("Enter your username:")
        password = input("Enter your password:")
        
        for user in data:
            if username == user[0] and password == user[1]:
                print("Login succesful!")
                atm_menu(user)
                return
            
    def atm_menu(user):
        while True:
            print("\nATM Menu:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Logout")
            choice = input("Enter your choice (1-4):")
            
            if choice == '1':
                print(f"Your current balance is: ${user[2]}")
            elif choice == '2':
                amount = float(input("Enter deposit amount:"))
                user[2] += amount
                print(f"${amount} deposited successfully!")
            elif choice == '3':
                amount = float(input("Enter withdrawal amount:"))
                if amount > user[2]:
                    print("Insufficient funds!")
                else:
                    user[2] -= amount
                    print(f"${amount} withdrawn successfully!")
            elif choice == '4':
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")