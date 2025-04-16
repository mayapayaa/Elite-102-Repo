def show_menu():
    print("\n=== Welcome to Prosperitas Bank ===")
    print("1. Log In")
    print("2. Create New Account")
    print("3. Exit")

def login():
    print("\n=== Log In ===")
    account_number = input("Enter your account number: ")
    pin = input("Enter your PIN: ")
    print("Login functionality coming soon...")

def create_account():
    print("\n=== Create New Account ===")
    name = input("Enter your full name: ")
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    pin = input("Choose a 4-digit PIN: ")
    print(f"Account creation for {name} coming soon...")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            login()
        elif choice == "2":
            create_account()
        elif choice == "3":
            print("Thanks for visiting Prosperitas Bank. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()