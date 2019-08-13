from src.main.python.com.revature.controller import menu
import logging
from src.main.python.com.revature.service import deposit, withdrawals, transaction_history, balance


def main():
    print("Welcome to the system")
    print('''
        1- Check Balance
        2- Deposit Money 
        3- Withdraw Money
        4- View Transactions
        5- System Logout''')

    ans = input("Please make a selection: ")

    if ans == '1':
        print("--------")
        print("Check Balance:")
        balance.main()
        # calls the balance check module
    elif ans == '2':
        print("---------")
        print("Deposit Money:")
        deposit.main()
        # calls the deposit module
    elif ans == '3':
        print("---------")
        print("Withdraw Money:")
        # calls on the withdrawls module
        withdrawals.main()
    elif ans == '4':
        print("---------")
        print("View Transaction History: ")
        # calls the transaction history module
        balance.main()
    elif ans == '5':
        print("Thank you for using PygBank")
        menu.main()
        logging.info("User Logged Out")
    else:
        print("Invalid Selection, returning to login")
        logging.error("Invalid menu selection")


if __name__ == '__main__':
    main()
