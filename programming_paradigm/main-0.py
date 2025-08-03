import sys
from bank_account import BankAccount

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <initial_balance> <command>[:<amount>]")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    try:
        initial_balance = float(sys.argv[1])
    except ValueError:
        print("Initial balance must be a number.")
        sys.exit(1)

    account = BankAccount(initial_balance)

    command_arg = sys.argv[2]
    command, *params = command_arg.split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        print(account.display_balance())
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
