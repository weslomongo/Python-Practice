balance = 1000.00
pin = "1234"
transactions = []


def login():
    attempts = 3

    while attempts > 0:
        entered_pin = input("\nEnter PIN: ")

        if entered_pin == pin:
            print("\nLogin Succesful.")
            return True

        else:
            attempts -= 1
            print(f"\nIncorrect PIN. {attempts} attempts remaining")

    print("\nToo many failed attempts. Account locked.")
    return False


def check_balance():
    print(f"\nChecking: ${balance:,.2f}")


def deposit():
    global balance

    try:
        amount = float(input("Enter amount: $"))

        if amount < 0:
            print("Deposit amount must be greater than zero.")
            return

        balance += amount
        transactions.append(f"Deposit: +${amount:,.2f}")
        print(f"Deposit succesful. New balance: ${balance:,.2f}")

    except ValueError:
        print("Please enter a valid amount.")


def withdraw():
    global balance

    try:
        amount = float(input("Enter amount: $"))

        if amount < 0:
            print("Deposit amount must be greater than zero.")

        elif amount > balance:
            print("Insufficent funds.")

        else:
            balance -= amount
            transactions.append(f"\nWithdrawl: -${amount:,.2f}")
            print(f"Withdrawl successful. Balance: ${balance:,.2f}")

    except ValueError:
        print("Please enter a valid amount.")


def transaction_history():
    print("\n----- Transaction History -----")

    if not transactions:
        print("No transactions.")

    else:
        for transaction in transactions:
            print()
            print(transaction)

def atm_menu():
    while True:
        print("\n===== ATM MENU =====\n" \
        "1. Check Balance\n" \
        "2. Deposit\n" \
        "3. Withdraw\n" \
        "4. Transaction History\n" \
        "5. Exit\n" \
        "====================")

        choice = input("Select an option: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            transaction_history()

        elif choice == "5":
            print("\nThank you! Goodbye.")
            break

        else:
            print("Invalid selection. Try again.")


if login():
    atm_menu()