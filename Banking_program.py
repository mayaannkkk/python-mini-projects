# Banking Program in python

def print_menu():
    print("1.Show_Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    print()


def show_balance(balance):
    print(f"Your balance is {balance:.2f}")
    print()


def deposit():
    amount = float(input("Enter Amount to be deposit:"))
    if amount < 0:
        print("Deposit a valid amount")
        return 0
    else:
        return amount


def withdraw(balance):
    amount = float(input("Enter amount to be withdrawal:"))
    if amount > balance:
        print("Insufficient Balance!")
        return 0
    elif amount < 0:
        print("Enter a valid amount")
        return 0
    else:
        return amount


def main():
    balance = 0
    while 1:
        print_menu()
        choice = int(input("Enter your choice:"))
        if choice < 1 or choice > 4:
            print("Enter a valid choice!!")
            continue

        if choice == 4:
            break

        match choice:
            case 1:
                show_balance(balance)
            case 2:
                balance += deposit()
            case 3:
                balance -= withdraw(balance)


if __name__ == '__main__':
    main()
